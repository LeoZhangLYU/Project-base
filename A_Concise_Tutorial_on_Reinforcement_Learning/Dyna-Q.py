from dynamic_programming import get_state,move
from Sarsa import get_action,get_update
import numpy as np
import random

# 初始化在每一个格子里采取每个动作的分数，初始化都是0，因为没有任何的知识
Q = np.zeros([4,12,4]) # 4行12列4个

# 保存历史数据，键是(row,col,action)，值是(next_row,next_col,reward)
history = dict()

def q_planing():
    # 计划10次
    for _ in range(20):
        # 随机选择一个历史数据
        row,col,action = random.choice(list(history.keys()))
        next_row,next_col,reward = history[(row,col,action)]

        # 选择下一个动作
        next_action = get_action(next_row,next_col)

        # 更新Q值
        update = get_update(row,col,action,reward,next_row,next_col,next_action)
        Q[row,col,action] += update

# 训练
def train():
    for _ in range(300):
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

            # 保存历史数据
            history[(row,col,action)] = (next_row,next_col,reward)

            # 选择下一个动作
            next_action = get_action(next_row,next_col)

            # 更新Q值
            update = get_update(row,col,action,reward,next_row,next_col,next_action)
            Q[row,col,action] += update

            # 反刍历史数据，进行离线学习
            q_planing()

            # 进入下一个状态
            row = next_row
            col = next_col
            action = next_action

        if _ % 10 == 0:
            print("Episode {}, reward total is {}".format(_,reward_sum))

if __name__ == '__main__':
    train()
    # 打印最终的Q值
    print("最终的Q值:")
    print(Q)

