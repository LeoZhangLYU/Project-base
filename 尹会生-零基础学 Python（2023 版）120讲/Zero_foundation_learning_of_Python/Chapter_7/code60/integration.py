# NOTE: 继承
class Father(object):
    def run(self, name):
        print(f"{name} 加油")
        pass


class Child(Father):
    def run(self, name):
        super(Child, self).run(name)
        print("run")


son = Child()
son.run("son")

# NOTE: 多继承
#  菱形继承时，Python会按照C3算法（有向无环路图）按顺序遍历继承图
#  通过类对象名称.__mro__可以查看继承顺序
#  多重继承增加了继承的复杂度，应当减少多重继承的使用
print(Child.__mro__)

# NOTE: 混入
#  混入Mix-In是指借用多继承的语法，为现有类增加新的方法
#  混入不定义新的属性，只包含方法
#  混入便于重用，但绝不能实例化
#  混入类一般在类名称后增加Mixin
