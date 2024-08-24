# NOTE: Python3.5以上版本
#  def func(变量名:类型)->返回类型:
#      return 变量名
def foo2(n1: int, n2: int) -> float:
    return n1 + n2


result = foo2(100, 200)
print(result)

# NOTE: 关键字参数
result = foo2(n1=100, n2=400)
print(result)


# NOTE: 默认值
#  使用关键字参数的函数，往往参数较多
#  当用户调用函数时，希望有大量参数采用默认值
#  定义函数时，可以直接为参数指定默认值
def foo3(n1: int = 100, n2: int = 200, n3: int = 300) -> float:
    return n1 + n2 + n3


print(foo3())
