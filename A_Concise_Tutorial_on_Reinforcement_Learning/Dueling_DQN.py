import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
import torch.nn.functional as F


# =================== 1. 环境创建 ===================
def make_env(render_mode=None):
    """创建 Pendulum 环境"""
    env = gym.make('Pendulum-v1', render_mode=render_mode)
    observation, info = env.reset()
    print(f"初始状态: {observation}")  # [cos(theta), sin(theta), theta_dot]
    return env


# 创建训练环境（不渲染）
env = make_env(render_mode=None)

# =================== 2. Dueling DQN 网络定义 ===================
N_STATES = 3
N_ACTIONS = 11
ACTION_SPACE = np.linspace(-2.0, 2.0, N_ACTIONS)

# note: 所有继承自 nn.Module 的类，其对象被调用时会自动执行 forward 方法。
class DuelingDQN(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dim=128):
        super(DuelingDQN, self).__init__()
        # 共享层
        self.feature = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )

        # 价值分支 (Value)
        self.value_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, 1)
        )

        # 优势分支 (Advantage)
        self.advantage_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, action_dim)
        )

    def forward(self, x):
        x = self.feature(x)
        value = self.value_head(x)  # [B, 1]
        advantage = self.advantage_head(x)  # [B, N_ACTIONS]
        # Dueling 合并公式
        q_values = value + (advantage - advantage.mean(dim=1, keepdim=True))
        return q_values


# 创建主网络和目标网络
model = DuelingDQN(N_STATES, N_ACTIONS)
next_model = DuelingDQN(N_STATES, N_ACTIONS)
next_model.load_state_dict(model.state_dict())  # 参数初始化一致

# =================== 3. 经验回放缓冲区 ===================
replay_buffer = []


# =================== 4. 核心函数 ===================

def get_action(state, model, epsilon=0.0):
    """根据 epsilon-greedy 策略选择动作"""
    if random.random() < epsilon:
        action_idx = random.randint(0, N_ACTIONS - 1)
    else:
        state_tensor = torch.FloatTensor(state).unsqueeze(0)  # [1, 3]
        with torch.no_grad():
            q_values = model(state_tensor)
            action_idx = q_values.argmax().item()

    action_continuous = ACTION_SPACE[action_idx]
    return action_idx, action_continuous


def update_data(env, replay_buffer, n_steps=200, model=None, epsilon=0.1):
    """收集 n_steps 步数据加入经验池"""
    initial_size = len(replay_buffer)

    while len(replay_buffer) - initial_size < n_steps:
        obs, info = env.reset()
        terminated = truncated = False

        while not (terminated or truncated):
            action_idx, action_cont = get_action(obs, model, epsilon)
            next_obs, reward, terminated, truncated, info = env.step(np.array([action_cont]))

            # 保存经验
            replay_buffer.append((obs, action_idx, reward, next_obs, terminated or truncated))
            obs = next_obs

            if terminated or truncated:
                break

    # 限制经验池大小
    while len(replay_buffer) > 10000:
        replay_buffer.pop(0)

    added = len(replay_buffer) - initial_size
    return added


def sample_batch(replay_buffer, batch_size=64):
    """从经验池中采样一个 batch"""
    if len(replay_buffer) < batch_size:
        return None  # 数据不足时返回 None

    batch = random.sample(replay_buffer, batch_size)
    states = torch.FloatTensor([e[0] for e in batch])
    actions = torch.LongTensor([e[1] for e in batch]).unsqueeze(1)
    rewards = torch.FloatTensor([e[2] for e in batch]).unsqueeze(1)
    next_states = torch.FloatTensor([e[3] for e in batch])
    dones = torch.FloatTensor([e[4] for e in batch]).unsqueeze(1)

    return states, actions, rewards, next_states, dones


def compute_q_values(model, states, actions):
    """计算当前 Q 值: Q(s,a)"""
    q_values = model(states)
    return q_values.gather(1, actions)


def compute_double_dqn_target_q(model, next_model, rewards, next_states, dones, gamma=0.99):
    """
    计算 Double DQN 的目标 Q 值
    target_q = r + γ * Q_target(s', argmax_a Q_main(s', a))
    """
    with torch.no_grad():
        # Step 1: 用主网络选择下一个状态的最优动作
        next_actions = model(next_states).argmax(dim=1, keepdim=True)  # [B, 1]

        # Step 2: 用目标网络评估这个动作的价值
        next_q_values = next_model(next_states).gather(1, next_actions)  # [B, 1]

        # Step 3: 构造目标
        target_q = rewards + gamma * next_q_values * (1 - dones)
    return target_q


def test(env_render_mode='human', n_episodes=1):
    """测试模型性能，可选择是否渲染"""
    test_env = gym.make('Pendulum-v1', render_mode=env_render_mode)
    total_rewards = []

    for _ in range(n_episodes):
        obs, info = test_env.reset()
        total_reward = 0
        done = False

        while not done:
            action_idx, action_cont = get_action(obs, model, epsilon=0.0)  # 不探索
            obs, reward, terminated, truncated, info = test_env.step(np.array([action_cont]))
            total_reward += reward
            done = terminated or truncated

        total_rewards.append(total_reward)

    test_env.close()
    return np.mean(total_rewards)


# =================== 5. 训练主循环 ===================
def train():
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.SmoothL1Loss()  # Huber Loss，更鲁棒
    epsilon = 1.0
    gamma = 0.99

    print("开始预填充经验池...")
    update_data(env, replay_buffer, n_steps=1000, model=model, epsilon=1.0)
    print(f"预填充完成，当前经验池大小: {len(replay_buffer)}")

    for episode in range(200):
        # 衰减 epsilon
        epsilon = max(0.05, 0.995 * epsilon)

        # 收集新数据
        added = update_data(env, replay_buffer, n_steps=200, model=model, epsilon=epsilon)

        # 训练 200 次
        for step in range(200):
            batch = sample_batch(replay_buffer, batch_size=64)
            if batch is None:
                continue

            states, actions, rewards, next_states, dones = batch

            # 计算当前 Q 值
            current_q = compute_q_values(model, states, actions)

            # 使用 Double DQN 计算目标 Q 值
            target_q = compute_double_dqn_target_q(model, next_model, rewards, next_states, dones, gamma)

            # 计算损失
            loss = loss_fn(current_q, target_q)

            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 定期更新目标网络（硬更新）
            if (step + 1) % 50 == 0:
                next_model.load_state_dict(model.state_dict())

        # 每 10 轮测试一次
        if (episode + 1) % 10 == 0:
            avg_reward = test(n_episodes=10)
            print(
                f"Episode {episode + 1:3d} | Epsilon: {epsilon:.3f} | "
                f"Replay: {len(replay_buffer)} | Avg Reward: {avg_reward:.2f}"
            )

        # 每 50 轮可视化一次
        if (episode + 1) % 50 == 0:
            print(f"Episode {episode + 1}: 可视化测试...")
            test(env_render_mode='human', n_episodes=1)

    print("训练完成，模型未保存。")


# =================== 6. 启动训练 ===================
if __name__ == '__main__':
    train()