# NOTE:
#  __init__()称作初始化方法，用于属性和方法初始化
#  在类实例化时自动进行初始化
#  初始化方法还可以让类实例化时接收参数
class Klass(object):
    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age

    def info(self):
        print(f"name: {self.name}, age: {self.age}")


People = Klass(name="People", age=20)

People.info()

# NOTE: 魔术方法
#  魔术方法时扩展现有数据类型的最佳实践
#  __init__()函数在类的编写中经常用于初始化和参数化处理
#  扩展数据类型默认的功能时，应有限考虑魔术方法
print(dir(int))
print(int(2).__gt__(11))  # 2 > 11?
