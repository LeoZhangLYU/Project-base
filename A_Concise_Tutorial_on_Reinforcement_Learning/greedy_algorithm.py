import numpy as np
import random

# 每个老虎机的中奖概率，0-1之间的均匀分布
probs = np.random.uniform(size=10)

# 记录每个老虎机的返回值
rewards = [[1] for _ in range(10)]

# 贪婪算法
def choose_one():
    # 有小概率随机选择一个老虎机
    if random.random() < 0.1:
        return random.choice(range(10))

    # 计算每个老虎机的平均返回值
    averages = [np.mean(rewards[i]) for i in range(10)]

    # 选择平均返回值最高的老虎机
    return np.argmax(averages)

def try_and_play():
    # 选择一个老虎机
    i = choose_one()

    reward = 0
    # 根据老虎机的中奖概率决定是否中奖
    if random.random() < probs[i]:
        reward = 1

    # 记录玩的结果
    rewards[i].append(reward)

def get_result():

    # 玩N次
    for _ in range(5000):
        try_and_play()

    # 期望的最好结果
    best = np.max(probs) * 5000

    # 实际结果
    actual = np.sum([np.sum(rewards[i]) for i in range(10)])

    print(f"期望的最好结果: {best}, 实际结果: {actual}")

if __name__ == "__main__":
    get_result()