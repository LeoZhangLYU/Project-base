import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import gymnasium as gym


# =================== 1. 环境创建 ===================
def make_env(render_mode=None):
    """创建 Pendulum 环境"""
    env = gym.make('Pendulum-v1', render_mode=render_mode)
    observation, info = env.reset(seed=0)
    print(f"初始状态: {observation}")
    return env


# 创建训练环境（不渲染）
env = make_env(render_mode=None)


# =================== 2. Actor-Critic 网络定义 ===================
class Actor(nn.Module):
    def __init__(self, state_dim=3, hidden_dim=128):
        super(Actor, self).__init__()
        # 共享特征提取层
        self.feature = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.Tanh(),  # 使用 Tanh 有助于稳定训练
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh()
        )
        # 输出动作的均值 (mu)
        self.fc_mu = nn.Linear(hidden_dim, 1)  # 输出 [-1, 1]
        # 输出动作的标准差 (std)
        self.fc_std = nn.Sequential(
            nn.Linear(hidden_dim, 1),
            nn.Softplus()  # 保证 std > 0
        )

    def forward(self, x):
        x = self.feature(x)
        mu = torch.tanh(self.fc_mu(x)) * 2.0  # 缩放到 [-2, 2]
        std = self.fc_std(x) + 1e-5  # 防止为 0
        return mu, std


class Critic(nn.Module):
    def __init__(self, state_dim=3, hidden_dim=128):
        super(Critic, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 1)
        )

    def forward(self, x):
        return self.network(x)


# 实例化网络
actor = Actor()
critic = Critic()


# =================== 3. 核心函数 ===================
def select_action(actor, state):
    """根据策略网络选择动作"""
    state_tensor = torch.FloatTensor(state).unsqueeze(0)  # [1, 3]
    with torch.no_grad():
        mu, std = actor(state_tensor)
    dist = torch.distributions.Normal(mu, std)
    action = dist.sample()
    log_prob = dist.log_prob(action)
    return action.item(), log_prob.item()


def collect_trajectory(env, actor, critic):
    """收集一个完整 episode 的轨迹数据"""
    states, actions, rewards, log_probs, values, dones = [], [], [], [], [], []

    state, info = env.reset()
    terminated = truncated = False

    while not (terminated or truncated):
        action, log_prob = select_action(actor, state)
        next_state, reward, terminated, truncated, info = env.step([action])

        # 获取状态价值 V(s)
        state_tensor = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            value = critic(state_tensor).item()

        states.append(state)
        actions.append(action)
        rewards.append(reward)  # 使用原始奖励
        log_probs.append(log_prob)
        values.append(value)
        dones.append(terminated or truncated)

        state = next_state

    # 最后一个状态的估计值
    with torch.no_grad():
        last_state_tensor = torch.FloatTensor(state).unsqueeze(0)
        last_value = critic(last_state_tensor).item()

    return states, actions, rewards, log_probs, values, dones, last_value


def compute_gae(rewards, values, next_values, dones, gamma=0.99, lambda_gae=0.95):
    """
    计算 Generalized Advantage Estimation (GAE)
    """
    advantages = []
    gae = 0
    for i in reversed(range(len(rewards))):
        # TD Error
        delta = rewards[i] + gamma * next_values[i] * (1 - dones[i]) - values[i]
        # GAE
        gae = delta + gamma * lambda_gae * (1 - dones[i]) * gae
        advantages.insert(0, gae)
    advantages = torch.FloatTensor(advantages).unsqueeze(1)
    returns = advantages + torch.FloatTensor(values).unsqueeze(1)
    return advantages, returns


def test(env, actor, render_mode=None):
    """测试当前策略的表现"""
    test_env = gym.make('Pendulum-v1', render_mode=render_mode)
    state, info = test_env.reset()
    total_reward = 0
    terminated = truncated = False

    while not (terminated or truncated):
        state_tensor = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            mu, std = actor(state_tensor)
        dist = torch.distributions.Normal(mu, std)
        action = dist.sample().item()
        state, reward, terminated, truncated, info = test_env.step([action])
        total_reward += reward
        if render_mode == 'human':
            test_env.render()

    test_env.close()
    return total_reward


# =================== 4. 训练主循环 ===================
def train_ppo(
        env, actor, critic, num_episodes=1000,
        gamma=0.99, lambda_gae=0.95, epsilon_clip=0.2,
        epochs=10, lr=3e-4
        ):
    # 为 Actor 和 Critic 使用同一个优化器（或分开）
    optimizer = optim.Adam(
        [
            {'params': actor.parameters(), 'lr': lr},
            {'params': critic.parameters(), 'lr': lr}
        ]
    )

    for episode in range(num_episodes):
        # 收集轨迹
        states, actions, rewards, log_probs, values, dones, last_value = collect_trajectory(env, actor, critic)

        # 准备下一个状态的值（用于 GAE 计算）
        next_values = values[1:] + [last_value]

        # 计算优势函数和回报
        advantages, returns = compute_gae(rewards, values, next_values, dones, gamma, lambda_gae)

        # 转为张量
        states_tensor = torch.FloatTensor(np.array(states))
        actions_tensor = torch.FloatTensor(actions).unsqueeze(1)
        old_log_probs_tensor = torch.FloatTensor(log_probs).unsqueeze(1)
        returns_tensor = returns

        # 多次更新（使用同一条轨迹）
        for _ in range(epochs):
            mu, std = actor(states_tensor)
            dist = torch.distributions.Normal(mu, std)
            new_log_probs = dist.log_prob(actions_tensor)

            # 重要性采样比率
            ratio = torch.exp(new_log_probs - old_log_probs_tensor.detach())

            # PPO 截断目标
            surr1 = ratio * advantages
            surr2 = torch.clamp(ratio, 1 - epsilon_clip, 1 + epsilon_clip) * advantages
            actor_loss = -torch.min(surr1, surr2).mean()

            # Critic 损失
            values_pred = critic(states_tensor)
            critic_loss = F.mse_loss(values_pred, returns_tensor)

            # 总损失
            loss = actor_loss + 0.5 * critic_loss

            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            # 可选：梯度裁剪
            # torch.nn.utils.clip_grad_norm_(actor.parameters(), 0.5)
            # torch.nn.utils.clip_grad_norm_(critic.parameters(), 0.5)
            optimizer.step()

        # 每隔一定回合测试
        if (episode + 1) % 50 == 0:
            avg_reward = sum(test(env, actor) for _ in range(5)) / 5
            print(
                f"Episode {episode + 1:3d} | "
                f"Actor Loss: {actor_loss.item():.3f} | "
                f"Critic Loss: {critic_loss.item():.1f} | "
                f"Avg Test Reward: {avg_reward:.1f}"
                )

        # 每 200 轮可视化一次
        if (episode + 1) % 200 == 0:
            print(f"Episode {episode + 1}: 可视化测试...")
            vis_reward = test(env, actor, render_mode='human')
            print(f"Visualization Reward: {vis_reward:.1f}")


# =================== 5. 启动训练 ===================
if __name__ == '__main__':
    train_ppo(env, actor, critic, num_episodes=1000)