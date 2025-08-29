import random

from Sarsa import get_state,get_action,move
import numpy as np

# 初始化在每一个格子里采取每个动作的分数，初始化都是0，因为没有任何的知识
Q = np.zeros([4,12,4]) # 4行12列4个动作

# 初始化3个list，用来存储状态，动作，奖励的历史数据，因为后面要用这些数据来更新Q值
state_history = []
action_history = []
reward_history = []

# 获取5个时间步分别的奖励
def get_update_list(next_row,next_col,next_action):
    # 初始化的target是最后一个state和最后一个action的分数
    target = Q[next_row,next_col,next_action]

    # 计算每一步的target
    # 这里是从后往前计算的，因为每一步的target依赖于下一步的target
    # 每一步的target = reward + 折扣 * 下一步的target
    target_list = []
    for reward in reward_history[::-1]:
        target = reward + 0.9 * target
        target_list.append(target)
    target_list.reverse()

    # 计算每一步的value
    value_list = []
    for i in range(len(state_history)):
        row,col = state_history[i]
        action = action_history[i]
        value = Q[row,col,action]
        value_list.append(value)

    # 计算每一步的更新量
    update_list = []
    for i in range(len(state_history)):
        # 时序差分算法，当前state,action的分数 = 下一个state,next_action的分数 * 折扣 + reward
        # 此处的update是target - value，越接近0说明越接近目标
        update = target_list[i] - value_list[i]
        update *= 0.1 # 学习率
        update_list.append(update)

    return update_list

# 训练
def train():
    for episode in range(1000):
        # 初始化当前位置
        row = random.choice(range(4))
        col = 0

        # 第一个动作
        action = get_action(row,col)
        # 计算反馈的和，这个数字应该越来越小
        reward_sum = 0
        # 清空历史数据
        state_history.clear()
        action_history.clear()
        reward_history.clear()

        # 循环直到到达终点或者掉进陷阱
        while get_state(row,col) not in ['terminal','trap']:
            # 执行动作
            next_row,next_col,reward = move(row,col,action)
            reward_sum += reward
            # 求新的动作
            next_action = get_action(next_row,next_col)
            # 记录历史数据
            state_history.append((row,col))
            action_history.append(action)
            reward_history.append(reward)
            # 如果历史数据有5个了，就更新Q值
            if len(reward_history) == 5:
                # 计算分数
                update_list = get_update_list(next_row,next_col,next_action)

                # 只更新第一步的分数
                row,col = state_history[0]
                action = action_history[0]
                update = update_list[0]
                Q[row,col,action] += update

                # 删除第一步的历史数据
                state_history.pop(0)
                action_history.pop(0)
                reward_history.pop(0)

            # 更新当前位置
            row = next_row
            col = next_col
            action = next_action

        # 走到终点或者掉进陷阱后，更新剩余的历史数据
        while len(reward_history) > 0:
            update_list = get_update_list(next_row,next_col,next_action)
            row,col = state_history[0]
            action = action_history[0]
            update = update_list[0]
            Q[row,col,action] += update
            state_history.pop(0)
            action_history.pop(0)
            reward_history.pop(0)

        if episode % 100 == 0:
            print("episode:",episode," reward_sum:",reward_sum)

if __name__ == "__main__":
    train()
    # 打印最终的Q值
    print("最终的Q值:")
    print(Q)
