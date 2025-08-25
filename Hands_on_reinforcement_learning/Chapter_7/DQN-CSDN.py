"""
文件名: 7.1
作者: 墨尘
日期: 2025/7/22
项目名: d2l_learning
备注: DQN算法在CartPole环境中的实现（适配Gym最新版本）
"""

import gymnasium as gym  # 推荐显式使用 gymnasium
import torch.nn.functional as F
import torch.optim as optim
import torch.nn as nn
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import torch
import collections
import random


class ReplayBuffer:
    """经验回放池：存储并采样过往经验"""

    def __init__(self, capacity):
        self.buffer = collections.deque(maxlen=capacity)  # 用双端队列实现，自动维护容量

    def add(self, state, action, reward, next_state, done):
        """添加一条经验到回放池"""
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        """随机采样一批经验"""
        transitions = random.sample(self.buffer, batch_size)
        # 解压成单独的列表
        state, action, reward, next_state, done = zip(*transitions)
        return np.array(state), action, reward, np.array(next_state), done

    def size(self):
        """返回当前回放池中的经验数量"""
        return len(self.buffer)


class Qnet(torch.nn.Module):
    """简单的Q网络（含一层隐藏层）"""

    def __init__(self, state_dim, hidden_dim, action_dim):
        super(Qnet, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_dim)  # 输入层→隐藏层
        self.fc2 = nn.Linear(hidden_dim, action_dim)  # 隐藏层→输出层

    def forward(self, x):
        """前向传播计算Q值"""
        x = F.relu(self.fc1(x))  # 隐藏层用ReLU激活
        return self.fc2(x)  # 输出层直接输出Q值


class DQN:
    """DQN算法实现（含目标网络）"""

    def __init__(
        self,
        state_dim,
        hidden_dim,
        action_dim,
        learning_rate,
        gamma,
        epsilon,
        target_update,
        device,
    ):
        self.action_dim = action_dim  # 动作维度
        self.device = device  # 设备（CPU/GPU）

        # 主Q网络（用于选择动作和更新）
        self.q_net = Qnet(state_dim, hidden_dim, action_dim).to(device)
        # 目标Q网络（用于计算目标Q值，定期从主网络复制参数）
        self.target_q_net = Qnet(state_dim, hidden_dim, action_dim).to(device)
        # 初始化目标网络参数（与主网络一致）
        self.target_q_net.load_state_dict(self.q_net.state_dict())
        # 优化器（Adam）
        self.optimizer = optim.Adam(self.q_net.parameters(), lr=learning_rate)

        self.gamma = gamma  # 折扣因子（未来奖励的衰减率）
        self.epsilon = epsilon  # ε-贪婪策略参数（探索率）
        self.target_update = target_update  # 目标网络更新频率
        self.count = 0  # 计数器（记录更新次数，用于触发目标网络更新）

    def take_action(self, state):
        """基于ε-贪婪策略选择动作"""
        if np.random.random() < self.epsilon:
            # 以ε概率随机选择动作（探索）
            action = np.random.randint(self.action_dim)
        else:
            # 以1-ε概率选择当前Q值最大的动作（利用）
            state = torch.tensor([state], dtype=torch.float).to(self.device)
            action = self.q_net(state).argmax().item()  # 取最大Q值对应的动作
        return action

    def update(self, transition_dict):
        """用一批经验更新Q网络"""
        # 从字典中提取数据并转换为Tensor
        states = torch.tensor(transition_dict["states"], dtype=torch.float).to(
            self.device
        )
        actions = (
            torch.tensor(transition_dict["actions"]).view(-1, 1).to(self.device)
        )  # 转为列向量
        rewards = (
            torch.tensor(transition_dict["rewards"], dtype=torch.float)
            .view(-1, 1)
            .to(self.device)
        )
        next_states = torch.tensor(
            transition_dict["next_states"], dtype=torch.float
        ).to(self.device)
        dones = (
            torch.tensor(transition_dict["dones"], dtype=torch.float)
            .view(-1, 1)
            .to(self.device)
        )  # 0/1表示是否终止

        # 计算当前状态的Q值（主网络）
        q_values = self.q_net(states).gather(1, actions)  # 按动作索引提取Q值

        # 计算目标Q值（用目标网络的下一状态最大Q值）
        max_next_q = (
            self.target_q_net(next_states).max(1)[0].view(-1, 1)
        )  # 下一状态的最大Q值
        q_targets = rewards + self.gamma * max_next_q * (
            1 - dones
        )  # 目标Q值（考虑终止状态）

        # 计算损失（均方误差）
        loss = F.mse_loss(q_values, q_targets)

        # 反向传播更新参数
        self.optimizer.zero_grad()  # 清空梯度
        loss.backward()  # 计算梯度
        self.optimizer.step()  # 更新参数

        # 定期更新目标网络（每target_update次更新一次）
        self.count += 1
        if self.count % self.target_update == 0:
            self.target_q_net.load_state_dict(self.q_net.state_dict())


if __name__ == "__main__":
    # 超参数设置
    lr = 2e-3  # 学习率
    num_episodes = 500  # 总训练回合数
    hidden_dim = 128  # 隐藏层维度
    gamma = 0.98  # 折扣因子
    epsilon = 0.01  # ε-贪婪策略（探索率）
    target_update = 10  # 目标网络更新频率
    buffer_size = 10000  # 经验回放池容量
    minimal_size = 500  # 开始训练的最小经验数
    batch_size = 64  # 每次训练的批大小

    # 设备设置（优先GPU，否则CPU）
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 创建环境（使用最新的CartPole-v1，避免v0的过时警告）
    env = gym.make("CartPole-v1")
    # 设置随机种子（适配Gym新版本：用reset(seed=...)替代env.seed()）
    seed = 0
    env.reset(seed=seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)

    # 获取状态维度和动作维度
    state_dim = env.observation_space.shape[0]  # CartPole的状态维度为4
    action_dim = env.action_space.n  # CartPole的动作维度为2（左/右）

    # 初始化经验回放池和DQN智能体
    replay_buffer = ReplayBuffer(buffer_size)
    agent = DQN(
        state_dim, hidden_dim, action_dim, lr, gamma, epsilon, target_update, device
    )

    # 训练过程
    return_list = []  # 记录每回合的总奖励
    for i in range(10):  # 分10个阶段显示进度
        # 用tqdm显示进度条
        with tqdm(total=int(num_episodes / 10), desc=f"Iteration {i}") as pbar:
            for i_episode in range(int(num_episodes / 10)):
                episode_return = 0  # 本回合的总奖励
                state, _ = (
                    env.reset()
                )  # 重置环境，获取初始状态（Gym新版本返回(state, info)）
                done = False

                while not done:
                    action = agent.take_action(state)  # 选择动作
                    next_state, reward, terminated, truncated, _ = env.step(
                        action
                    )  # 执行动作（Gym新版本返回5个值）
                    done = terminated or truncated  # 终止条件（要么达到目标，要么超时）
                    # 将经验加入回放池
                    replay_buffer.add(state, action, reward, next_state, done)
                    state = next_state  # 更新状态
                    episode_return += reward  # 累积奖励

                    # 当经验池中的样本足够时，开始训练
                    if replay_buffer.size() > minimal_size:
                        # 采样一批经验
                        b_s, b_a, b_r, b_ns, b_d = replay_buffer.sample(batch_size)
                        # 构造过渡字典
                        transition_dict = {
                            "states": b_s,
                            "actions": b_a,
                            "next_states": b_ns,
                            "rewards": b_r,
                            "dones": b_d,
                        }
                        # 更新DQN
                        agent.update(transition_dict)

                return_list.append(episode_return)  # 记录本回合奖励

                # 每10回合更新进度条信息
                if (i_episode + 1) % 10 == 0:
                    pbar.set_postfix(
                        {
                            "episode": f"{i * int(num_episodes / 10) + i_episode + 1}",
                            "avg_return": f"{np.mean(return_list[-10:]):.2f}",
                        }
                    )
                pbar.update(1)

    # 绘制训练曲线（如果有rl_utils可以用其绘图函数，否则注释）
    plt.figure(figsize=(10, 5))
    plt.plot(return_list)
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.title("DQN on CartPole-v1")
    plt.show()


class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = collections.deque(maxlen=capacity)

    def add(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        transitions = random.sample(self.buffer, batch_size)
        state, action, reward, next_state, done = zip(*transitions)
        return np.array(state), action, reward, np.array(next_state), done

    def size(self):
        return len(self.buffer)


def moving_average(a, window_size):
    cumulative_sum = np.cumsum(np.insert(a, 0, 0))
    middle = (
        cumulative_sum[window_size:] - cumulative_sum[:-window_size]
    ) / window_size
    r = np.arange(1, window_size - 1, 2)
    begin = np.cumsum(a[: window_size - 1])[::2] / r
    end = (np.cumsum(a[:-window_size:-1])[::2] / r)[::-1]
    return np.concatenate((begin, middle, end))


def train_on_policy_agent(env, agent, num_episodes):
    return_list = []
    for i in range(10):
        with tqdm(total=int(num_episodes / 10), desc="Iteration %d" % i) as pbar:
            for i_episode in range(int(num_episodes / 10)):
                episode_return = 0
                transition_dict = {
                    "states": [],
                    "actions": [],
                    "next_states": [],
                    "rewards": [],
                    "dones": [],
                }
                state = env.reset()
                done = False
                while not done:
                    action = agent.take_action(state)
                    next_state, reward, done, _ = env.step(action)
                    transition_dict["states"].append(state)
                    transition_dict["actions"].append(action)
                    transition_dict["next_states"].append(next_state)
                    transition_dict["rewards"].append(reward)
                    transition_dict["dones"].append(done)
                    state = next_state
                    episode_return += reward
                return_list.append(episode_return)
                agent.update(transition_dict)
                if (i_episode + 1) % 10 == 0:
                    pbar.set_postfix(
                        {
                            "episode": "%d" % (num_episodes / 10 * i + i_episode + 1),
                            "return": "%.3f" % np.mean(return_list[-10:]),
                        }
                    )
                pbar.update(1)
    return return_list


def train_off_policy_agent(
    env, agent, num_episodes, replay_buffer, minimal_size, batch_size
):
    return_list = []
    for i in range(10):
        with tqdm(total=int(num_episodes / 10), desc="Iteration %d" % i) as pbar:
            for i_episode in range(int(num_episodes / 10)):
                episode_return = 0
                state = env.reset()
                done = False
                while not done:
                    action = agent.take_action(state)
                    next_state, reward, done, _ = env.step(action)
                    replay_buffer.add(state, action, reward, next_state, done)
                    state = next_state
                    episode_return += reward
                    if replay_buffer.size() > minimal_size:
                        b_s, b_a, b_r, b_ns, b_d = replay_buffer.sample(batch_size)
                        transition_dict = {
                            "states": b_s,
                            "actions": b_a,
                            "next_states": b_ns,
                            "rewards": b_r,
                            "dones": b_d,
                        }
                        agent.update(transition_dict)
                return_list.append(episode_return)
                if (i_episode + 1) % 10 == 0:
                    pbar.set_postfix(
                        {
                            "episode": "%d" % (num_episodes / 10 * i + i_episode + 1),
                            "return": "%.3f" % np.mean(return_list[-10:]),
                        }
                    )
                pbar.update(1)
    return return_list


def compute_advantage(gamma, lmbda, td_delta):
    td_delta = td_delta.detach().numpy()
    advantage_list = []
    advantage = 0.0
    for delta in td_delta[::-1]:
        advantage = gamma * lmbda * advantage + delta
        advantage_list.append(advantage)
    advantage_list.reverse()
    return torch.tensor(advantage_list, dtype=torch.float)
