import numpy as np
import random
from dynamic_programming import move,get_state

# NOTE: 初始化在每一个格子里采取每个动作的分数，初始化都是0，因为没有任何的知识
Q = np.zeros([4,12,4]) # 4行12列4个动作

# NOTE: 根据状态选择一个动作
def get_action(row,col):
    # 小概率随机选择一个动作
    if random.random() < 0.1:
        return random.choice(range(4))
    return Q[row,col].argmax()

# NOTE: 更新分数，每次更新取决于当前的格子，当前的动作，下一个格子，下一个格子的动作
def get_update(row,col,action,reward,next_row,next_col,next_action):

    # 计算target
    # Sarsa算法
    target = 0.9 * Q[next_row,next_col,next_action]
    # Q-learning算法
    # target = 0.9 * Q[next_row,next_col].max()
    target += reward

    # 计算value
    value = Q[row,col,action]

    # 根据时序差分算法，当前state,action的分数 = 下一个state,next_action的分数 * 折扣 + reward
    update = target - value

    update *=0.1 # 学习率

    # 更新当前状态和动作的分数
    return update

# NOTE: 训练
def train():
    for episode in range(1000):
        # 初始化当前位置
        row = random.choice(range(4))
        col = 0

        # 第一个动作
        action = get_action(row,col)

        # 计算反馈的和，这个数字应该越来越小
        reward_sum = 0

        # 循环直到到达终点或者掉进陷阱
        while get_state(row,col) not in ['terminal','trap']:
            # 根据当前状态和动作，得到下一个状态和奖励
            next_row,next_col,reward = move(row,col,action)
            reward_sum += reward

            # 选择下一个动作
            next_action = get_action(next_row,next_col)

            # 更新Q值
            # Sarsa算法
            update = get_update(row,col,action,reward,next_row,next_col,next_action)
            # Q-learning算法
            # update = get_update(row,col,action,reward,next_row,next_col,None)
            Q[row,col,action] += update

            # 进入下一个状态，继续循环
            row = next_row
            col = next_col
            action = next_action
        if episode % 100 == 0:
            print(f"第{episode}次训练，奖励和={reward_sum}")

# 测试
def test():
    row = random.choice(range(4))
    col = 0
    step = 0
    while get_state(row,col) not in ['terminal','trap']:
        action = Q[row,col].argmax()
        print(f"第{step}步，位置=({row},{col})，动作={action}")
        row,col,reward = move(row,col,action)
        step += 1
    print(f"最终位置=({row},{col})，状态={get_state(row,col)}")

if __name__ == '__main__':
    train()
    test()
    # 打印最终的Q值
    print("最终的Q值:")
    print(Q)
