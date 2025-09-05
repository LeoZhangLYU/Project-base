import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import gymnasium as gym
import random
from collections import deque


# =================== 1. 环境创建 ===================
def make_env(render_mode=None):
    """创建 CartPole 环境"""
    env = gym.make('CartPole-v1', render_mode=render_mode)
    observation, info = env.reset(seed=0)
    print(f"初始状态: {observation}")
    return env


# 创建训练环境（不渲染）
env = make_env(render_mode=None)


# =================== 2. 网络定义 ===================
# Actor: 输出动作概率分布（策略网络）
actor = nn.Sequential(
    nn.Linear(4, 128),
    nn.ReLU(),
    nn.Linear(128, 2),  # 2 个动作
    nn.Softmax(dim=-1)  # 概率分布
)

# Critic: 评估状态-动作对的 Q 值（双网络）
class Critic(nn.Module):
    def __init__(self, state_dim=4, action_dim=2):
        super(Critic, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim)  # 输出每个动作的 Q 值
        )

    def forward(self, state):
        return self.network(state)


critic1 = Critic()
critic2 = Critic()
target_critic1 = Critic()
target_critic2 = Critic()

# 复制参数到目标网络
target_critic1.load_state_dict(critic1.state_dict())
target_critic2.load_state_dict(critic2.state_dict())


# =================== 3. 自动调节温度系数 alpha ===================
log_alpha = torch.zeros(1, requires_grad=True)
alpha_optimizer = optim.Adam([log_alpha], lr=3e-4)
target_entropy = -np.log(1.0 / 2)  # 离散动作：目标熵 = -log(1/n_actions)


# =================== 4. 经验回放缓冲区 ===================
class ReplayBuffer:
    def __init__(self, capacity=10000):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        states = torch.FloatTensor([e[0] for e in batch])
        actions = torch.LongTensor([e[1] for e in batch]).unsqueeze(1)
        rewards = torch.FloatTensor([e[2] for e in batch]).unsqueeze(1)
        next_states = torch.FloatTensor([e[3] for e in batch])
        dones = torch.FloatTensor([e[4] for e in batch]).unsqueeze(1)
        return states, actions, rewards, next_states, dones

    def __len__(self):
        return len(self.buffer)


replay_buffer = ReplayBuffer()


# =================== 5. 核心函数 ===================
def select_action(actor, state, deterministic=False):
    """根据策略选择动作"""
    state_tensor = torch.FloatTensor(state).unsqueeze(0)
    with torch.no_grad():
        action_probs = actor(state_tensor)[0]
    if deterministic:
        return action_probs.argmax().item()
    action = torch.multinomial(action_probs, 1).item()
    return action


def soft_update(target, source, tau=0.005):
    """软更新目标网络参数"""
    for target_param, param in zip(target.parameters(), source.parameters()):
        target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)


# =================== 6. 测试函数 ===================
def test(env, actor, n_episodes=5):
    """测试策略性能"""
    total_rewards = []
    for _ in range(n_episodes):
        state, info = env.reset()
        total_reward = 0
        terminated = truncated = False
        while not (terminated or truncated):
            action = select_action(actor, state, deterministic=True)
            state, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
        total_rewards.append(total_reward)
    return np.mean(total_rewards)


# =================== 7. 训练主循环 ===================
def train_dsac(env, actor, critic1, critic2, target_critic1, target_critic2,
               replay_buffer, num_episodes=1000, gamma=0.99, tau=0.005, batch_size=64):
    optimizer_actor = optim.Adam(actor.parameters(), lr=3e-4)
    optimizer_critic1 = optim.Adam(critic1.parameters(), lr=3e-4)
    optimizer_critic2 = optim.Adam(critic2.parameters(), lr=3e-4)

    for episode in range(num_episodes):
        # 收集一条轨迹
        state, info = env.reset()
        terminated = truncated = False

        while not (terminated or truncated):
            action = select_action(actor, state)
            next_state, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated

            replay_buffer.push(state, action, reward, next_state, done)
            state = next_state

        if len(replay_buffer) < batch_size:
            continue

        states, actions, rewards, next_states, dones = replay_buffer.sample(batch_size)

        # ---------------------
        #   Critic 更新
        # ---------------------
        with torch.no_grad():
            # 获取目标网络的 Q 值
            q1_next = target_critic1(next_states)  # [B, 2]
            q2_next = target_critic2(next_states)  # [B, 2]
            q_next = torch.min(q1_next, q2_next)   # [B, 2]

            # 计算目标策略的熵正则化 Q 值
            prob_next = actor(next_states)  # [B, 2]
            log_prob_next = torch.log(prob_next + 1e-6)  # [B, 2]
            v_next = (prob_next * (q_next - log_alpha.exp() * log_prob_next)).sum(dim=1, keepdim=True)  # [B, 1]

            td_target = rewards + gamma * (1 - dones) * v_next  # [B, 1]

        # 当前 Critic 预测
        q1 = critic1(states).gather(1, actions)  # [B, 1]
        q2 = critic2(states).gather(1, actions)  # [B, 1]

        critic_loss1 = F.mse_loss(q1, td_target)
        critic_loss2 = F.mse_loss(q2, td_target)

        optimizer_critic1.zero_grad()
        critic_loss1.backward()
        optimizer_critic1.step()

        optimizer_critic2.zero_grad()
        critic_loss2.backward()
        optimizer_critic2.step()

        # ---------------------
        #   Actor 更新
        # ---------------------
        prob = actor(states)  # [B, 2]
        log_prob = torch.log(prob + 1e-6)  # [B, 2]
        q1 = critic1(states)  # [B, 2]
        q2 = critic2(states)  # [B, 2]
        q = torch.min(q1, q2)  # [B, 2]

        actor_loss = (prob * (log_alpha.exp() * log_prob - q)).sum(dim=1).mean()

        optimizer_actor.zero_grad()
        actor_loss.backward()
        optimizer_actor.step()

        # ---------------------
        #   自动调节 alpha
        # ---------------------
        with torch.no_grad():
            entropy = -log_prob.detach() * prob  # [B, 2]
            entropy = entropy.sum(dim=1, keepdim=True)  # [B, 1]

        alpha_loss = -(log_alpha * (entropy - target_entropy).detach()).mean()

        alpha_optimizer.zero_grad()
        alpha_loss.backward()
        alpha_optimizer.step()

        # ---------------------
        #   软更新目标网络
        # ---------------------
        soft_update(target_critic1, critic1, tau)
        soft_update(target_critic2, critic2, tau)

        # ---------------------
        #   每 50 轮测试一次
        # ---------------------
        if (episode + 1) % 50 == 0:
            avg_reward = test(env, actor)
            current_alpha = log_alpha.exp().item()
            print(f"Episode {episode+1:3d} | "
                  f"Critic Loss: {(critic_loss1.item() + critic_loss2.item())/2:.3f} | "
                  f"Actor Loss: {actor_loss.item():.3f} | "
                  f"Alpha Loss: {alpha_loss.item():.3f} | "
                  f"Alpha: {current_alpha:.3f} | "
                  f"Avg Test Reward: {avg_reward:.1f}")


# =================== 8. 启动训练 ===================
if __name__ == '__main__':
    train_dsac(env, actor, critic1, critic2, target_critic1, target_critic2, replay_buffer, num_episodes=1000)