# NOTE: 类的装饰器
#  类的装饰器是类方法的装饰器的缩写

# NOTE: classmethod装饰器
#  可以将实例的方法定义为类的方法，用于类方法直接调用
class Klass1:
    @classmethod
    def funcs(cls):
        print("class method")


Klass1.funcs()


# NOTE: staticmethod装饰器
#  不需要类的任何信息，但又和类相关的一些方法，为了方便维护代码并保持代码工整，可以将该函数定义到类中并使用staticmethod修饰
class Klass2:
    @staticmethod
    def funcs():
        print("static method")


Klass2.funcs()


# NOTE: property
class Klass3:
    @property
    def func(self):
        return self.__varName

    @func.setter
    def func(self, val):
        self.__varName = val


obj = Klass3()
# obj.func() # 报错，无func()属性
obj.func = 123
print(obj.func)

# NOTE: 非必要，不要使用类的方法的装饰器
