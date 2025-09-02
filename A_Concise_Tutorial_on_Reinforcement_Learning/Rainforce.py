import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import gymnasium as gym


# =================== 1. 环境创建 ===================
def make_env(render_mode=None):
    """创建 CartPole 环境"""
    env = gym.make('CartPole-v1', render_mode=render_mode)
    observation, info = env.reset()
    print(f"初始状态: {observation}")  # [位置, 速度, 杆子角度, 杆子角速度]
    return env


# 创建训练环境（不渲染）
env = make_env(render_mode=None)

# =================== 2. 模型定义 ===================
model = nn.Sequential(
    nn.Linear(4, 128),
    nn.ReLU(),
    nn.Linear(128, 2),
    nn.Softmax(dim=1)  # 输出每个动作的概率
)

# =================== 3. 核心函数 ===================
def get_action(state, model):
    """根据策略网络输出的概率分布选择动作"""
    state_tensor = torch.FloatTensor(state).unsqueeze(0)  # [1, 4]
    with torch.no_grad():
        action_probs = model(state_tensor).numpy().flatten()  # [2]
    action = np.random.choice(2, p=action_probs)  # 动作空间大小为 2
    return action


def sample_episode(env, model):
    """采样一个完整的回合"""
    states, actions, rewards = [], [], []
    state, info = env.reset()
    terminated = truncated = False

    while not (terminated or truncated):
        action = get_action(state, model)
        next_state, reward, terminated, truncated, info = env.step(action)

        states.append(state)
        actions.append(action)
        rewards.append(reward)

        state = next_state

    return states, actions, rewards


def test(env, model):
    """测试模型性能"""
    state, info = env.reset()
    total_reward = 0
    terminated = truncated = False
    while not (terminated or truncated):
        state_tensor = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            action_probs = model(state_tensor).numpy().flatten()
        action = np.random.choice(2, p=action_probs)
        state, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
    return total_reward


# =================== 4. 训练 ===================
def train(env, model, n_episodes=1000, gamma=0.98, learning_rate=1e-3):
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    model.train()

    for episode in range(n_episodes):
        # 1. 采样一个 episode
        states, actions, rewards = sample_episode(env, model)

        # 2. 计算每个时间步的折扣回报 G_t（从后往前）
        returns = []
        G = 0
        for r in reversed(rewards):
            G = r + gamma * G
            returns.append(G)
        returns.reverse()  # 顺序变为 [G0, G1, ..., G_T-1]

        # 3. 计算总损失
        optimizer.zero_grad()  # 清零梯度
        total_loss = 0

        for state, action, G in zip(states, actions, returns):
            state_tensor = torch.FloatTensor(state).unsqueeze(0)  # [1, 4]
            action_probs = model(state_tensor)  # [1, 2]
            log_prob = torch.log(action_probs[0, action])  # log π(a|s)
            loss = -log_prob * G  # 策略梯度损失
            total_loss += loss

        # 4. 反向传播并更新
        total_loss.backward()
        optimizer.step()

        # 5. 每隔 100 轮测试一次
        if (episode + 1) % 100 == 0:
            avg_reward = np.mean([test(env, model) for _ in range(10)])
            print(f"回合 {episode+1:3d} | 平均奖励: {avg_reward:.2f}")


# =================== 5. 启动训练 ===================
if __name__ == '__main__':
    train(env, model)