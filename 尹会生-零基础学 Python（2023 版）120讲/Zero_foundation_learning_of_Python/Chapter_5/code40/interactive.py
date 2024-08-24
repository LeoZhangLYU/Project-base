# NOTE: 输入设备与输入方式
#  交互方式输入：input()函数
#  非交互方式输入：命令行参数、文件


import argparse

# 执行方式 python3 6-1arg-1.py -number 100
parser = argparse.ArgumentParser(description="这个程序用来演示参数处理")
# -number 表示 number 参数是可选参数
# number 表示 number 参数是必选参数
parser.add_argument("-number", help="输入一个数字", type=int, default=10)
# parser.add_argument("number", help="输入一个数字")
args = parser.parse_args()
print(f"你输入的number参数是：{args.number}")
