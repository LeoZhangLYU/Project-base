import gymnasium as gym  # 推荐显式使用 gymnasium
from Chapter_4.DP import PolicyIteration, print_agent, ValueIteration

# 创建环境
env = gym.make("FrozenLake-v1", render_mode="rgb_array")
env = env.unwrapped  # 解封装以访问内部属性 P

# 必须先 reset，才能 render
env.reset()

# 此时可以安全渲染
env.render()  # 不会再报错

# 接下来分析状态转移
holes = set()
ends = set()

for s in env.P:
    for a in env.P[s]:
        for s_ in env.P[s][a]:
            # s_[2] 是 reward, s_[3] 是 done
            if s_[2] == 1.0:  # 奖励为1，表示到达目标
                ends.add(s_[1])  # s_[1] 是 next_state
            if s_[3] == True:  # 到达终止状态（包括 hole 和 goal）
                holes.add(s_[1])

# 目标是奖励为1的终止状态；冰洞是终止但奖励不为1的
holes = holes - ends
print("冰洞的索引:", holes)
print("目标的索引:", ends)

# 查看目标左边一格（状态14）的状态转移
print("\n状态 14 的状态转移:")
for a in env.P[6]:
    print(f"动作 {a}: {env.P[6][a]}")


# 这个动作意义是Gym库针对冰湖环境事先规定好的
action_meaning = ["<", "v", ">", "^"]
theta = 1e-5
gamma = 0.9
agent = PolicyIteration(env, theta, gamma)
agent.policy_iteration()
print_agent(agent, action_meaning, [5, 7, 11, 12], [15])

agent = ValueIteration(env, theta, gamma)
agent.value_iteration()
print_agent(agent, action_meaning, [5, 7, 11, 12], [15])
