import gymnasium as gym
import numpy as np
from gymnasium.envs.toy_text.frozen_lake import generate_random_map


def make_env():
    # 创建冰湖环境 - 修复：移除map_name参数
    env = gym.make(
        "FrozenLake-v1",
        is_slippery=False,  # 开启滑动随机性（冰面会打滑）
        render_mode="human",  # 以可视化模式渲染
        desc=['SFFF', 'FHFH', 'FFFH', 'HFFG'],  # 自定义地图
    )

    # 重置环境并获取初始状态
    observation, info = env.reset(seed=42)  # 设置随机种子确保可复现
    print(f"初始状态: {observation}")  # 状态是0-15的整数（4*4地图）

    return env, observation, info, ['SFFF', 'FHFH', 'FFFH', 'HFFG']


# 手动实现状态转移概率函数 - 替代env.P
def get_transition_probabilities(state, action, desc, is_slippery=True):
    """获取给定状态和动作下的所有可能转移"""
    nrow, ncol = len(desc), len(desc[0])
    row, col = divmod(state, ncol)

    # 定义动作效果 (0=左, 1=下, 2=右, 3=上)
    actions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # 辅助函数：获取下一个状态（考虑边界）
    def get_next_state(r, c, a):
        nr, nc = r + actions[a][0], c + actions[a][1]
        nr = max(0, min(nrow - 1, nr))
        nc = max(0, min(ncol - 1, nc))
        return nr * ncol + nc

    # 如果不滑动，直接返回确定性转移
    if not is_slippery:
        next_state = get_next_state(row, col, action)
        next_row, next_col = divmod(next_state, ncol)
        cell_type = desc[next_row][next_col]
        reward = 1.0 if cell_type == 'G' else 0.0
        terminated = (cell_type == 'G' or cell_type == 'H')
        return [(1.0, next_state, reward, terminated)]

    # 滑动模式：2/3概率执行预期动作，1/6概率向左滑，1/6概率向右滑
    # 注意：在FrozenLake中，"滑"是指转向垂直方向
    probabilities = []
    intended = action
    left = (action + 1) % 4  # 注意：FrozenLake中，左滑是+1（不是-1）
    right = (action - 1) % 4

    for a, prob in [(intended, 2 / 3), (left, 1 / 6), (right, 1 / 6)]:
        next_state = get_next_state(row, col, a)
        next_row, next_col = divmod(next_state, ncol)
        cell_type = desc[next_row][next_col]
        reward = 1.0 if cell_type == 'G' else 0.0
        terminated = (cell_type == 'G' or cell_type == 'H')
        probabilities.append((prob, next_state, reward, terminated))

    return probabilities


# 计算qsa - 修复：添加必要参数
def get_qsa(state, action, values, desc, is_slippery=True, gamma=0.9):
    value = 0.0
    transitions = get_transition_probabilities(state, action, desc, is_slippery)

    for prob, next_state, reward, terminated in transitions:
        if terminated:
            value += prob * reward
        else:
            value += prob * (reward + gamma * values[next_state])
    return value


# 策略评估 - 修复：添加必要参数
def get_values(values, pi, desc, is_slippery=True, gamma=0.9, algorithm='policy_iteration'):
    new_values = np.zeros(16)
    for state in range(16):
        action_values = np.zeros(4)
        for action in range(4):
            action_values[action] = get_qsa(state, action, values, desc, is_slippery, gamma)

        if algorithm == 'policy_iteration':
            new_values[state] = np.sum(pi[state] * action_values)
        else:  # value_iteration
            new_values[state] = np.max(action_values)
    return new_values


# 策略提升 - 修复：添加必要参数
def improve_policy(values, desc, is_slippery=True, gamma=0.9):
    new_pi = np.zeros([16, 4])
    for state in range(16):
        action_values = np.zeros(4)
        for action in range(4):
            action_values[action] = get_qsa(state, action, values, desc, is_slippery, gamma)

        best_actions = np.argwhere(action_values == np.max(action_values)).flatten()
        for action in best_actions:
            new_pi[state, action] = 1 / len(best_actions)
    return new_pi


if __name__ == '__main__':
    env, observation, info, desc = make_env()
    is_slippery = False  # 与环境创建时保持一致

    # 初始化每个格子的价值
    values = np.zeros(16)  # 4x4地图有16个状态

    # 初始化每个格子下采用动作的概率
    pi = np.ones([16, 4]) / 4  # 每个状态4个动作，初始均匀分布

    # 选择迭代方式
    algorithm = 'policy_iteration'  # 'value_iteration' 或 'policy_iteration'
    gamma = 0.9  # 折扣因子

    # 迭代直到收敛
    for i in range(100):  # 最大迭代次数
        # 策略评估
        for _ in range(100):
            new_values = get_values(values, pi, desc, is_slippery, gamma, algorithm)
            # 检查收敛
            if np.max(np.abs(new_values - values)) < 1e-6:
                break
            values = new_values.copy()

        # 策略提升
        old_pi = pi.copy()
        pi = improve_policy(values, desc, is_slippery, gamma)

        # 检查策略是否收敛
        if np.array_equal(pi, old_pi):
            print(f"策略在迭代 {i + 1} 后收敛")
            break

    print("最终策略 (每个状态的最佳动作概率):")
    print(pi)
    print("\n状态值函数:")
    print(values.reshape(4, 4))

    # 清理资源
    env.close()