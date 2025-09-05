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
    """创建 Pendulum 环境"""
    env = gym.make('Pendulum-v1', render_mode=render_mode)
    observation, info = env.reset(seed=0)
    print(f"初始状态: {observation}")
    return env


# 创建训练环境（不渲染）
env = make_env(render_mode=None)


# =================== 2. Actor 和 Critic 网络定义 ===================
class Actor(nn.Module):
    def __init__(self, state_dim=3, action_dim=1, hidden_dim=128):
        super(Actor, self).__init__()
        # 共享特征层
        self.feature = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )
        # 输出动作的均值 (mu)
        self.fc_mu = nn.Linear(hidden_dim, action_dim)
        # 输出动作的标准差 (std)
        self.fc_std = nn.Linear(hidden_dim, action_dim)

    def forward(self, state):
        x = self.feature(state)
        mu = self.fc_mu(x)
        log_std = self.fc_std(x)
        log_std = torch.clamp(log_std, -20, 2)  # 数值稳定
        std = torch.exp(log_std)

        # 从正态分布中采样
        normal = torch.distributions.Normal(mu, std)
        # 重参数化技巧
        z = normal.rsample()
        # 将动作映射到 [-2, 2] 范围
        action = torch.tanh(z) * 2.0

        # 计算对数概率（考虑 tanh 变换的雅可比行列式）
        log_prob = normal.log_prob(z) - torch.log(1 - action.tanh().pow(2) + 1e-6)
        log_prob = log_prob.sum(dim=1, keepdim=True)

        return action, log_prob


class Critic(nn.Module):
    def __init__(self, state_dim=3, action_dim=1, hidden_dim=128):
        super(Critic, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim + action_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )

    def forward(self, state, action):
        x = torch.cat([state, action], dim=1)
        return self.network(x)


# 实例化网络
actor = Actor()
critic1 = Critic()
critic2 = Critic()
target_critic1 = Critic()
target_critic2 = Critic()

# 复制参数到目标网络
target_critic1.load_state_dict(critic1.state_dict())
target_critic2.load_state_dict(critic2.state_dict())


# =================== 3. 自动调节温度系数 alpha ===================
# 温度系数 alpha 控制探索程度
log_alpha = torch.zeros(1, requires_grad=True)
alpha_optimizer = optim.Adam([log_alpha], lr=3e-4)
target_entropy = -1.0  # 对于连续动作空间，目标熵通常设为 -action_dim


# =================== 4. 经验回放缓冲区 ===================
class ReplayBuffer:
    def __init__(self, capacity=100000):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        states = torch.FloatTensor([e[0] for e in batch])
        actions = torch.FloatTensor([e[1] for e in batch]).unsqueeze(1)
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
    state_tensor = torch.FloatTensor(state).unsqueeze(0)  # [1, 3]
    with torch.no_grad():
        action, _ = actor(state_tensor)
    if deterministic:
        return action.item()
    return action.item()  # SAC 的探索由策略本身的随机性保证


def soft_update(target, source, tau=0.005):
    """软更新目标网络参数"""
    for target_param, param in zip(target.parameters(), source.parameters()):
        target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)


# =================== 6. 测试函数 ===================
def test(env, actor, n_episodes=1):
    """测试策略性能"""
    total_rewards = []
    for _ in range(n_episodes):
        state, info = env.reset()
        total_reward = 0
        terminated = truncated = False
        while not (terminated or truncated):
            action = select_action(actor, state, deterministic=True)
            state, reward, terminated, truncated, info = env.step([action])
            total_reward += reward
        total_rewards.append(total_reward)
    return np.mean(total_rewards)


# =================== 7. 训练主循环 ===================
def train_sac(env, actor, critic1, critic2, target_critic1, target_critic2,
              replay_buffer, num_episodes=1000, gamma=0.99, tau=0.005, batch_size=64):
    # 优化器
    optimizer_actor = optim.Adam(actor.parameters(), lr=3e-4)
    optimizer_critic1 = optim.Adam(critic1.parameters(), lr=3e-4)
    optimizer_critic2 = optim.Adam(critic2.parameters(), lr=3e-4)

    for episode in range(num_episodes):
        # 收集一条轨迹
        state, info = env.reset()
        terminated = truncated = False

        while not (terminated or truncated):
            action = select_action(actor, state)
            next_state, reward, terminated, truncated, info = env.step([action])
            done = terminated or truncated

            # 存入经验池
            replay_buffer.push(state, action, reward, next_state, done)
            state = next_state

        # 如果经验池不够，跳过训练
        if len(replay_buffer) < batch_size:
            continue

        # 采样一个 batch
        states, actions, rewards, next_states, dones = replay_buffer.sample(batch_size)

        # ---------------------
        #   Critic 更新
        # ---------------------
        with torch.no_grad():
            # 目标网络选择下一个动作及其对数概率
            next_actions, next_log_probs = actor(next_states)
            # 目标 Critic 评估 Q 值
            q1_next = target_critic1(next_states, next_actions)
            q2_next = target_critic2(next_states, next_actions)
            q_next = torch.min(q1_next, q2_next)
            # TD Target
            td_target = rewards + gamma * (1 - dones) * (q_next - log_alpha.exp() * next_log_probs)

        # 当前 Critic 预测
        q1 = critic1(states, actions)
        q2 = critic2(states, actions)
        critic_loss1 = F.mse_loss(q1, td_target)
        critic_loss2 = F.mse_loss(q2, td_target)

        # 更新 Critic
        optimizer_critic1.zero_grad()
        critic_loss1.backward()
        optimizer_critic1.step()

        optimizer_critic2.zero_grad()
        critic_loss2.backward()
        optimizer_critic2.step()

        # ---------------------
        #   Actor 更新
        # ---------------------
        predicted_actions, log_probs = actor(states)
        q1_new = critic1(states, predicted_actions)
        q2_new = critic2(states, predicted_actions)
        q_new = torch.min(q1_new, q2_new)
        # 最大化熵正则化的回报
        actor_loss = (log_alpha.exp() * log_probs - q_new).mean()

        optimizer_actor.zero_grad()
        actor_loss.backward()
        optimizer_actor.step()

        # ---------------------
        #   自动调节 alpha
        # ---------------------
        alpha_loss = (-log_alpha * (log_probs + target_entropy).detach()).mean()

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
            avg_reward = test(env, actor, n_episodes=5)
            current_alpha = log_alpha.exp().item()
            print(f"Episode {episode+1:3d} | "
                  f"Critic Loss: {(critic_loss1.item() + critic_loss2.item())/2:.3f} | "
                  f"Actor Loss: {actor_loss.item():.3f} | "
                  f"Alpha Loss: {alpha_loss.item():.3f} | "
                  f"Alpha: {current_alpha:.3f} | "
                  f"Avg Test Reward: {avg_reward:.1f}")


# =================== 8. 启动训练 ===================
if __name__ == '__main__':
    train_sac(env, actor, critic1, critic2, target_critic1, target_critic2, replay_buffer, num_episodes=1000)