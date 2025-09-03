import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import gymnasium as gym
import random
from Rainforce import make_env


# =================== 1. 环境创建 ===================

# 创建训练环境（不渲染）
env = make_env(render_mode=None)

# =================== 2. 网络定义 ===================
# Actor: 输出动作概率分布
actor = nn.Sequential(
    nn.Linear(4, 128),
    nn.ReLU(),
    nn.Linear(128, 2),
    nn.Softmax(dim=1)
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
        action_probs = actor(state_tensor).squeeze(0).numpy()  # [2]
    action = np.random.choice(2, p=action_probs)  # 根据概率采样
    return action


def collect_trajectory(env, actor):
    """收集一个完整 episode 的轨迹数据"""
    states, actions, rewards, next_states, dones = [], [], [], [], []

    state, info = env.reset()
    terminated = truncated = False

    while not (terminated or truncated):
        action = select_action(actor, state)
        next_state, reward, terminated, truncated, info = env.step(action)

        states.append(state)
        actions.append(action)
        rewards.append(reward)
        next_states.append(next_state)
        dones.append(terminated or truncated)

        state = next_state

    # 转换为张量
    states = torch.FloatTensor(np.array(states))  # [T, 4]
    actions = torch.LongTensor(np.array(actions)).unsqueeze(1)  # [T, 1]
    rewards = torch.FloatTensor(rewards).unsqueeze(1)  # [T, 1]
    next_states = torch.FloatTensor(np.array(next_states))  # [T, 4]
    dones = torch.FloatTensor(dones).unsqueeze(1)  # [T, 1]

    return states, actions, rewards, next_states, dones


def evaluate_policy(env, actor, n_episodes=1):
    """测试策略性能"""
    total_rewards = []
    for _ in range(n_episodes):
        state, info = env.reset()
        episode_reward = 0
        terminated = truncated = False
        while not (terminated or truncated):
            action = select_action(actor, state)
            state, reward, terminated, truncated, info = env.step(action)
            episode_reward += reward
        total_rewards.append(episode_reward)
    return np.mean(total_rewards)


# =================== 4. 训练主循环 ===================
def train_actor_critic(env, actor, critic, num_episodes=100, gamma=0.99, lr=1e-3):
    optimizer_actor = optim.Adam(actor.parameters(), lr=lr)
    optimizer_critic = optim.Adam(critic.parameters(), lr=lr)
    mse_loss = nn.MSELoss()

    for episode in range(num_episodes):
        # 收集一条轨迹
        states, actions, rewards, next_states, dones = collect_trajectory(env, actor)

        # ---------------------
        #   Critic 更新：学习状态价值
        # ---------------------
        with torch.no_grad():
            # TD Target: r + γ * V(s')
            td_target = rewards + gamma * critic(next_states) * (1 - dones)

        # 当前 Critic 对 V(s) 的预测
        current_value = critic(states)

        # 值函数损失
        value_loss = mse_loss(current_value, td_target)

        # 更新 Critic
        optimizer_critic.zero_grad()
        value_loss.backward()
        optimizer_critic.step()

        # ---------------------
        #   Actor 更新：基于优势函数改进策略
        # ---------------------
        with torch.no_grad():
            # 优势函数 A(s,a) ≈ TD Error = r + γV(s') - V(s)
            advantage = td_target - current_value

        # 获取当前策略下动作的概率
        action_probs = actor(states)  # [T, 2]
        selected_action_probs = action_probs.gather(1, actions)  # [T, 1]

        # 策略梯度损失（使用对数概率 × 优势）
        # 加上 1e-8 防止 log(0)
        policy_loss = -torch.log(selected_action_probs + 1e-8) * advantage.detach()
        policy_loss = policy_loss.mean()

        # 更新 Actor
        optimizer_actor.zero_grad()
        policy_loss.backward()
        optimizer_actor.step()

        # ---------------------
        #   日志输出
        # ---------------------
        if (episode + 1) % 10 == 0:
            avg_reward = evaluate_policy(env, actor, n_episodes=5)
            print(
                f"Episode {episode + 1:3d} | "
                f"Value Loss: {value_loss.item():.3f} | "
                f"Policy Loss: {policy_loss.item():.3f} | "
                f"Avg Reward: {avg_reward:.2f}"
                )


# =================== 5. 启动训练 ===================
if __name__ == '__main__':
    train_actor_critic(env, actor, critic, num_episodes=100)