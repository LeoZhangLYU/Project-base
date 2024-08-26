# NOTE: try-except代码块
try:
    1 / 0
except ZeroDivisionError:
    print("除数不能为0")

num = 1
num2 = 0
try:
    num / num2
except ZeroDivisionError:
    print("上一段程序有异常")
except Exception as e:
    print("上一段程序有异常")
    print(e)
else:
    print("try部分的代码没有抛出异常，执行此代码")
finally:
    print("无论是否抛出异常，该部分代码均会执行")
