import numpy as np
import random

# 每个老虎机的中奖概率，0-1之间的均匀分布
probs = np.random.uniform(size=10)

# 记录每个老虎机的返回值
rewards = [[1] for _ in range(10)]

# 贪婪算法
def choose_one():
    # 有小概率随机选择一个老虎机
    # if random.random() < 0.1:
    #     return random.choice(range(10))

    # OPTIMIZE: 贪婪算法的改进，随机选择的概率逐渐下降
    played_count = sum(len(rewards[i]) for i in range(10))
    if random.random()<1/played_count:
        return random.choice(range(10))

    # 计算每个老虎机的平均返回值
    averages = [np.mean(rewards[i]) for i in range(10)]

    # 选择平均返回值最高的老虎机
    return np.argmax(averages)

# OPTIMIZE: UCB算法，更多的探索玩的更少的老虎机
def choose_one_ucb():
    # 求出每个老虎机各自的玩的次数
    played_counts = np.array([len(rewards[i]) for i in range(10)])

    # 求出上置信界
    # 分子是总共完了多少次，取根号后让他的增长更慢
    # 分母是每台老虎机玩的次数，乘以2让他增长更快
    # 随着玩的次数越多，分母会很快超过分子的增长速度，导致分数越来越小
    # 具体到每个老虎机上，就是玩的次数越多，上置信界越小
    # 所以ucb衡量了每台老虎机的不确定性，玩的次数越少，不确定性越大，上置信界越高
    fenzi = np.sqrt(np.log(sum(played_counts)))
    fenmu = played_counts*2
    ucb = fenzi / fenmu

    # 大于1的ucb会被缩小，小于1的ucb会被放大，保持ucb恒定在一定的数值范围内
    ucb = ucb**0.5

    # 计算每个老虎机的平均返回值
    averages = [np.mean(rewards[i]) for i in range(10)]
    scores = averages + ucb

    return np.argmax(scores)

# 汤普森采样算法，使用beta分布衡量期望
def choose_one_beta():
    # 求出每个老虎机出1的次数
    count_1 = [sum(rewards[i]) for i in range(10)]

    # 求出每个老虎机出0的次数
    count_0 = [len(rewards[i]) - count_1[i] for i in range(10)]

    # 对每个老虎机，根据beta分布采样一个值
    samples = [np.random.beta(count_1[i] + 1, count_0[i] + 1) for i in range(10)]

    return np.argmax(samples)


def try_and_play():
    # 选择一个老虎机
    # i = choose_one()
    # i= choose_one_ucb()
    i= choose_one_beta()


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