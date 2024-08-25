# NOTE: 函数对象和函数调用
from functools import reduce, partial


def foo():
    print("foo函数执行")


foo()
var = foo
var()


# NOTE: 高阶函数
#  高阶函数通常指的是map、filter、reduce
#  map、filter是内置函数，可以直接使用
#  reduce需要通过fuctools库导入

# NOTE: map(函数，可迭代对象):将可迭代对象的每个元素都作为函数参数执行
def add(number):
    return number + number


print([x for x in map(add, range(1, 11))])

# NOTE: filter(函数，可迭代对象)：过滤掉可迭代对象中返回值不为True的元素
print(list(filter(lambda x: x % 2 == 0, range(1, 11))))

# NOTE: reduce(函数，可迭代对象):对可迭代对象进行累积
print(reduce(lambda x, y: x + y * 2, range(1, 11)))

# NOTE: 偏函数：固定某个参数，形成新的函数
new_func = partial(add, 10)
print(new_func())
