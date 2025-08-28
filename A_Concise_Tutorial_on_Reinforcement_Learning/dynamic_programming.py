import numpy as np

# 获取一个格子的状态
def get_state(row,col):
    if row!=3:
        return "ground"

    if row==3 and col==0:
        return "ground"

    if row==3 and col==11:
        return "terminal"

    return "trap"

# 在一个格子里做一个动作
def move(row,col,action):
    # 如果当前已经在陷阱或者终点，则不能执行任何动作，反馈都是0
    if get_state(row,col) in ["trap","terminal"]:
        return row,col,0

    # ↑
    if action==0:
        row -= 1

    # ↓
    if action==1:
        row += 1

    # ←
    if action==2:
        col -= 1

    # →
    if action==3:
        col += 1

    # 保证不出界
    row = max(0,min(3,row))
    col = max(0,min(11,col))

    # 根据新的格子状态，决定反馈
    # 陷阱奖励为-100，否则都是-1，强迫机器人尽快找到终点，因为每走一步都是负奖励
    reward = -1
    if get_state(row,col)=="trap":
        reward = -100

    return row,col,reward

# 初始化每个格子的价值
values = np.zeros([4,12])

# 初始化每个格子下采用动作的概率
pi = np.ones([4,12,4]) * 0.25

# 计算在一个状态下执行动作的分数
def get_qsa(row,col,action):
    # 在当前状态下执行动作，得到下一个状态和奖励
    next_row,next_col,reward = move(row,col,action)

    # 计算下一个状态的分数，取values当中记录的分数即可，0.9是折扣因子
    value = 0.9 * values[next_row,next_col]

    # 如果下一个状态是终点或者陷阱，则不考虑下一个状态的分数
    if get_state(next_row,next_col) in ["trap","terminal"]:
        value = 0

    # 动作的分数本身就是rewared + 下一个状态的分数
    return value+reward

# 策略评估
def get_value():
    # 初始化一个新的values，重新评估所有格子的分数
    new_values = np.zeros([4,12])
    # 遍历所有格子
    for row in range(4):
        for col in range(12):
            # 计算当前格子4个动作分别的分数
            action_value = np.zeros(4)
            for action in range(4):
                action_value[action] = get_qsa(row,col,action)
            # 根据当前格子下4个动作的概率，计算当前格子的分数
            new_values[row,col] = (action_value * pi[row,col]).sum()
    return new_values

# 策略提升
def get_pi():
    # 重新初始化每个格子下采用动作的概率，重新评估
    new_pi = np.zeros([4,12,4])
    # 遍历所有格子
    for row in range(4):
        for col in range(12):
            # 计算当前格子4个动作分别的分数
            action_value = np.zeros(4)
            # 遍历所有动作
            for action in range(4):
                action_value[action] = get_qsa(row,col,action)
            # 计算当前格子下最优动作的个数
            max_count = (action_value==action_value.max()).sum()
            # 最优动作的概率是1/max_count，其他动作概率是0
            for action in range(4):
                if action_value[action]==action_value.max():
                    new_pi[row,col,action] = 1/max_count
                else:
                    new_pi[row,col,action] = 0
    return new_pi

# 训练
if __name__ == '__main__':
    for i in range(10):
        for j in range(100):
            values = get_value()
        pi = get_pi()

    print("最终的格子分数:")
    print(values)
    print("最终的策略:")
    directions = ["↑","↓","←","→"]
    for row in range(4):
        line = ""
        for col in range(12):
            action = pi[row,col].argmax()
            line += directions[action] + " "
        print(line)

