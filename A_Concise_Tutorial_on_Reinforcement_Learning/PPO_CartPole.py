from itertools import chain

import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


# =================== 1. 环境创建 ===================
def make_env(render_mode=None):
    """创建 CartPole 环境"""
    env = gym.make('CartPole-v1', render_mode=render_mode)
    observation, info = env.reset()
    print(f"初始状态: {observation}")
    return env


# 创建训练环境（不渲染）
env = make_env(render_mode=None)

# =================== 2. 网络定义 ===================
# Actor: 输出动作概率分布
actor = nn.Sequential(
    nn.Linear(4, 128),
    nn.ReLU(),
    nn.Linear(128, 2),
    nn.Softmax(dim=-1)  # 沿最后一个维度归一化
)

# Critic: 输出状态价值 V(s)
critic = nn.Sequential(
    nn.Linear(4, 128),
    nn.ReLU(),
    nn.Linear(128, 1)
)


# =================== 3. 核心函数 ===================
def select_action(actor, state):
    """根据策略网络选择动作"""
    state_tensor = torch.FloatTensor(state).unsqueeze(0)  # [1, 4]
    with torch.no_grad():
        action_probs = actor(state_tensor)  # [1, 2]

    # 使用 PyTorch 的概率分布采样（推荐做法）
    dist = torch.distributions.Categorical(action_probs)
    action = dist.sample()  # 返回 [1]
    log_prob = dist.log_prob(action)  # 记录 log_prob 用于更新

    return action.item(), log_prob.item()


def collect_trajectory(env, actor, critic):
    """收集一个完整 episode 的轨迹数据"""
    states, actions, rewards, log_probs, values, next_states, dones = [], [], [], [], [], [], []

    state, info = env.reset()
    terminated = truncated = False

    while not (terminated or truncated):
        action, log_prob = select_action(actor, state)
        next_state, reward, terminated, truncated, info = env.step(action)

        # 获取状态价值 V(s)
        state_tensor = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            value = critic(state_tensor).item()

        states.append(state)
        actions.append(action)
        rewards.append(reward)
        log_probs.append(log_prob)
        values.append(value)
        next_states.append(next_state)
        dones.append(terminated or truncated)

        state = next_state

    # 最后一个状态的估计值（用于 GAE 计算）
    with torch.no_grad():
        last_state_tensor = torch.FloatTensor(next_state).unsqueeze(0)
        last_value = critic(last_state_tensor).item()

    return states, actions, rewards, log_probs, values, dones, last_value


def compute_advantages(rewards, values, dones, last_value, gamma=0.99, lambda_gae=0.95):
    """
    使用 GAE（Generalized Advantage Estimation）计算优势函数
    """
    advantages = []
    gae = 0

    # 从后往前计算
    for i in reversed(range(len(rewards))):
        if i == len(rewards) - 1:
            next_value = last_value
        else:
            next_value = values[i + 1]

        # TD Error: δ = r + γV(s') - V(s)
        td_error = rewards[i] + gamma * next_value * (1 - dones[i]) - values[i]

        # GAE: A = δ + (γλ) * A_next
        gae = td_error + gamma * lambda_gae * (1 - dones[i]) * gae
        advantages.insert(0, gae)

    # 转为张量
    advantages = torch.FloatTensor(advantages).unsqueeze(1)
    returns = advantages + torch.FloatTensor(values).unsqueeze(1)  # R = A + V

    return advantages, returns


def test(env, actor):
    """测试当前策略的表现"""
    state, info = env.reset()
    total_reward = 0
    terminated = truncated = False

    while not (terminated or truncated):
        state_tensor = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            action_probs = actor(state_tensor)
        dist = torch.distributions.Categorical(action_probs)
        action = dist.sample().item()
        state, reward, terminated, truncated, info = env.step(action)
        total_reward += reward

    return total_reward


# =================== 4. 训练主循环 ===================
def train_ppo(
        env, actor, critic, num_episodes=1000, gamma=0.99, lambda_gae=0.95,
        epsilon_clip=0.2, epochs=10, batch_size=64, lr=1e-3
        ):
    optimizer = optim.Adam(chain(actor.parameters(),critic.parameters()), lr=lr)
    # 也可以为 actor 和 critic 分别设置优化器

    for episode in range(num_episodes):
        # 收集一条轨迹
        states, actions, rewards, log_probs, values, dones, last_value = collect_trajectory(env, actor, critic)

        # 计算优势函数和回报
        advantages, returns = compute_advantages(rewards, values, dones, last_value, gamma, lambda_gae)

        # 将数据转换为张量
        states_tensor = torch.FloatTensor(np.array(states))
        actions_tensor = torch.LongTensor(actions).unsqueeze(1)
        old_log_probs_tensor = torch.FloatTensor(log_probs).unsqueeze(1)
        returns_tensor = returns

        # PPO 更新：多次使用同一条轨迹数据
        for _ in range(epochs):
            # 当前策略的输出
            action_probs = actor(states_tensor)  # [T, 2]
            dist = torch.distributions.Categorical(action_probs)
            # NOTE: unsqueeze(x) 和 squeeze(x) 的作用是增加或减少维度为1的第x维度
            new_log_probs = dist.log_prob(actions_tensor.squeeze(1)).unsqueeze(1)  # [T, 1]
            values_pred = critic(states_tensor)  # [T, 1]

            # 计算重要性采样比率 r(θ)
            ratio = torch.exp(new_log_probs - old_log_probs_tensor.detach())  # [T, 1]

            # PPO 截断目标
            surr1 = ratio * advantages
            surr2 = torch.clamp(ratio, 1 - epsilon_clip, 1 + epsilon_clip) * advantages
            actor_loss = -torch.min(surr1, surr2).mean()

            # Critic 损失：预测值 vs 目标回报
            critic_loss = F.mse_loss(values_pred, returns_tensor)

            # 总损失（可分开优化）
            loss = actor_loss + 0.5 * critic_loss

            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # 每隔一定回合测试一次
        if (episode + 1) % 50 == 0:
            avg_reward = test(env, actor)
            print(
                f"Episode {episode + 1:3d} | "
                f"Actor Loss: {actor_loss.item():.3f} | "
                f"Critic Loss: {critic_loss.item():.3f} | "
                f"Test Reward: {avg_reward:.1f}"
                )


# =================== 5. 启动训练 ===================
if __name__ == '__main__':
    train_ppo(env, actor, critic, num_episodes=500)