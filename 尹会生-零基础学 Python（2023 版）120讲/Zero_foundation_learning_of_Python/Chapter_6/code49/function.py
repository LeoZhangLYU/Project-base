def foo():
    print("foo")


print("aaaa")

foo()

# NOTE: 匿名函数
#  匿名函数是借用lambda表达式进行函数的定义和调用
add_1 = lambda x: x + 1
print(add_1)


# 等于
def add_1(x):
    return x + 1


print(add_1(100))
