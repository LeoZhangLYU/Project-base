import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
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
    def __init__(self, state_dim=3, action_dim=1, hidden_dim=64):
        super(Actor, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
            nn.Tanh()  # 输出 [-1, 1]
        )

    def forward(self, state):
        action = self.network(state)
        return action * 2.0  # 缩放到 [-2, 2]


class Critic(nn.Module):
    def __init__(self, state_dim=3, action_dim=1, hidden_dim=64):
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
critic = Critic()
target_actor = Actor()
target_critic = Critic()

# 复制参数到目标网络
target_actor.load_state_dict(actor.state_dict())
target_critic.load_state_dict(critic.state_dict())


# =================== 3. 经验回放缓冲区 ===================
class ReplayBuffer:
    def __init__(self, capacity=10000):
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


# =================== 4. 核心函数 ===================
def select_action(actor, state, noise_std=0.1):
    """根据策略选择动作，并添加噪声以增加探索"""
    state_tensor = torch.FloatTensor(state).unsqueeze(0)  # [1, 3]
    with torch.no_grad():
        action = actor(state_tensor).item()
    # 添加高斯噪声
    noise = np.random.normal(0, noise_std)
    action = np.clip(action + noise, -2.0, 2.0)  # 确保在合法范围内
    return action


def soft_update(target, source, tau=0.005):
    """软更新目标网络参数"""
    for target_param, param in zip(target.parameters(), source.parameters()):
        target_param.data.copy_(tau * param.data + (1 - tau) * target_param.data)


# =================== 5. 测试函数 ===================
def test(env, actor, n_episodes=1):
    """测试策略性能"""
    total_rewards = []
    for _ in range(n_episodes):
        state, info = env.reset()
        total_reward = 0
        terminated = truncated = False
        while not (terminated or truncated):
            action = select_action(actor, state, noise_std=0.0)  # 测试时不加噪声
            state, reward, terminated, truncated, info = env.step([action])
            total_reward += reward
        total_rewards.append(total_reward)
    return np.mean(total_rewards)


# =================== 6. 训练主循环 ===================
def train_ddpg(env, actor, critic, target_actor, target_critic, replay_buffer,
               num_episodes=1000, gamma=0.99, tau=0.005, noise_std=0.1, batch_size=64):
    optimizer_actor = optim.Adam(actor.parameters(), lr=1e-3)
    optimizer_critic = optim.Adam(critic.parameters(), lr=1e-3)
    mse_loss = nn.MSELoss()

    for episode in range(num_episodes):
        # 收集一条轨迹
        state, info = env.reset()
        terminated = truncated = False

        while not (terminated or truncated):
            action = select_action(actor, state, noise_std=noise_std)
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
            next_actions = target_actor(next_states)  # 目标 Actor 选择动作
            target_q = target_critic(next_states, next_actions)  # 目标 Critic 评估价值
            td_target = rewards + gamma * target_q * (1 - dones)

        current_q = critic(states, actions)
        critic_loss = mse_loss(current_q, td_target)

        optimizer_critic.zero_grad()
        critic_loss.backward()
        optimizer_critic.step()

        # ---------------------
        #   Actor 更新
        # ---------------------
        predicted_actions = actor(states)
        actor_loss = -critic(states, predicted_actions).mean()  # 最大化 Q 值

        optimizer_actor.zero_grad()
        actor_loss.backward()
        optimizer_actor.step()

        # ---------------------
        #   软更新目标网络
        # ---------------------
        soft_update(target_actor, actor, tau)
        soft_update(target_critic, critic, tau)

        # ---------------------
        #   每 50 轮测试一次
        # ---------------------
        if (episode + 1) % 50 == 0:
            avg_reward = test(env, actor, n_episodes=5)
            print(f"Episode {episode+1:3d} | "
                  f"Critic Loss: {critic_loss.item():.3f} | "
                  f"Actor Loss: {actor_loss.item():.3f} | "
                  f"Avg Test Reward: {avg_reward:.1f}")


# =================== 7. 启动训练 ===================
if __name__ == '__main__':
    train_ddpg(env, actor, critic, target_actor, target_critic, replay_buffer, num_episodes=1000)