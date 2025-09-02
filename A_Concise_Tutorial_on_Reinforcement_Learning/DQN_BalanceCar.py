import random

import gymnasium as gym
import torch

# 创建 CartPole 环境
env = gym.make('CartPole-v1', render_mode='human')  # 使用 'human' 模式可视化

# 重置环境，获取初始状态
observation, info = env.reset()

# 计算动作的模型，也是真正要用的模型,输出是一个长度为 2 的向量，表示在每个动作（0: 左，1: 右）上的“得分”或“Q 值”
model = torch.nn.Sequential(torch.nn.Linear(4,128),torch.nn.ReLU(),torch.nn.Linear(128,2))

# 经验网络，用于评估一个状态的分数
next_model = torch.nn.Sequential(torch.nn.Linear(4,128),torch.nn.ReLU(),torch.nn.Linear(128,2))
next_model.load_state_dict(model.state_dict()) # 让经验网络的参数和动作网络一样

def get_action(observation):
    if random.random() < 0.1:
        return random.choice([0,1])

    # 计算动作
    state = torch.FloatTensor(observation).reshape(1,4)

    return model(state).argmax().item()

# 样本池
replay_buffer = []

# 向样本池中添加样本N条，删除最早的N条
def add_to_replay_buffer(N:int=200):
    replay_buffer_size = len(replay_buffer)

    # 新增N条数据
    while len(replay_buffer) - replay_buffer_size < N:
        # 初始化游戏
        observation, info = env.reset()

        # 循环直到游戏结束
        terminated = False
        while not terminated:
            # 选择动作
            action = get_action(observation)

            # 执行动作
            next_observation, reward, terminated, truncated, info = env.step(action)

            # 保存样本 (state, action, reward, next_state, done)
            replay_buffer.append((observation, action, reward, next_observation, terminated or truncated))

            # 进入下一个状态
            observation = next_observation

    update_count = len(replay_buffer) - replay_buffer_size
    drop_count = max(0, len(replay_buffer) - 10000)

    # 数据上限，删除最早的drop_count条
    for _ in range(drop_count):
        replay_buffer.pop(0)

    return update_count,drop_count

# 获取一批数据样本
def get_batch(batch_size=64):
    # 随机选择batch_size个样本
    batch = random.sample(replay_buffer, batch_size)

    # 将样本转换为张量
    states = torch.FloatTensor([sample[0] for sample in batch])
    actions = torch.LongTensor([sample[1] for sample in batch]).reshape(-1,1)
    rewards = torch.FloatTensor([sample[2] for sample in batch]).reshape(-1,1)
    next_states = torch.FloatTensor([sample[3] for sample in batch])
    dones = torch.FloatTensor([sample[4] for sample in batch]).reshape(-1,1)

    return states, actions, rewards, next_states, dones

def get_value(states,action):
    # 计算当前状态下，执行动作的分数
    q_values = model(states)

    # 根据实际执行的动作，选择对应的分数
    # gather函数的作用是从q_values中选择对应动作的分数
    # 这里的1表示按列选择，actions是一个列向量，表示每个样本选择的动作
    # 结果是一个列向量，表示每个样本在选择的动作上的分数
    # 这个值就是模型评估的当前状态和动作的分数
    # 在执行动作前，显然并不知道动作的分数和下一个状态，所以这里不能也不需要考虑下一个状态
    return q_values.gather(1,action)

def test(play):
    # 初始化游戏
    state, info = env.reset()
    # 记录总奖励
    total_reward = 0

    # 玩到游戏结束为止
    terminated = False
    while not terminated:
        # 选择动作
        action = get_action(state)
        # 执行动作
        next_state, reward, terminated, truncated, info = env.step(action)
        # 累计奖励
        total_reward += reward
        # 打印动画
        if play and random.random() < 0.1:
            env.render()
    return total_reward

def get_target(reward, next_state, over):
    with torch.no_grad(): # 临时关闭 PyTorch 的梯度计算功能，用于推理（inference）或不需要反向传播的场景。
        target = next_model(next_state)           # [b, 2]
        target = target.max(dim=1)[0].reshape(-1, 1)  # [b, 1]: 最大 Q 值
        target *= 0.98                            # 折扣因子
        target *= (1 - over)                      # 若结束则设为 0
        target += reward                          # 加上当前奖励
    return target

def train():
    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=2e-3)
    loss_fn = torch.nn.MSELoss()

    # =============== 新增：预填充 replay buffer ===============
    print("Pre-filling replay buffer...")
    update_count, drop_count = add_to_replay_buffer(N=200)  # 添加至少 200 条经验
    print(f"Added {update_count} samples to replay buffer.")
    if len(replay_buffer) == 0:
        raise RuntimeError("Failed to add samples to replay buffer!")

    # 训练 500 次
    for epoch in range(500):
        for iteration in range(200):
            # 采样数据
            states, actions, rewards, next_states, dones = get_batch()

            # 计算当前状态和动作的分数
            values = get_value(states, actions)
            # 计算目标分数
            targets = get_target(rewards, next_states, dones)

            # 计算损失
            loss = loss_fn(values, targets)
            # print(f"Iteration {iteration}, loss: {loss.item()}")
            # 反向传播，更新模型参数
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 每隔 10 次迭代，更新一次经验网络
            if iteration % 10 == 0:
                next_model.load_state_dict(model.state_dict())

        if epoch % 50 == 0:
            test_result = sum([test(play=False) for _ in range(20)]) / 20
            print(f"Epoch {epoch}, test result: {test_result}")

if __name__ == '__main__':
    train()