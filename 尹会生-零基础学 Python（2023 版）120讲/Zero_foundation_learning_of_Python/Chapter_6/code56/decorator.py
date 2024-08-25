# NOTE: LEGB规则
import time

number = 100


def foo():
    number = 200
    print(f"函数内部{number}")


foo()
print(f"函数外部：{number}")


# NOTE:
#  函数内的再次定义的内部函数形成闭包
#  闭包作用域之内，内部函数可以访问外部函数的变量
def out():
    number = 300

    def infunc():
        print(f"闭包变量：{number}")
        return number

    return infunc


out()()

# NOTE: 装饰器语法：引入@语法实现函数嵌套定义
#  python内置的装饰器使用了functools包
#  常用的有：
#   @lru_cache 缓存
#   @wraps  被装饰函数保持原对象不变

# 以计算函数运行时间为例
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__}函数一共执行了{end - start}秒")

    return wrapper


@time_it
def work():
    print("work 函数开始执行")
    time.sleep(2)
    print("work 函数结束执行")


work()
print(work.__name__)
