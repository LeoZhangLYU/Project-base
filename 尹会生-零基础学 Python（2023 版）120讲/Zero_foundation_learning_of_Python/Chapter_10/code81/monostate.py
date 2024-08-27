# NOTE: 创建型模式
#  创建型模式的典型设计模式：单例模式
#  单实例模式可以由import来实现
#  可以借助类属性实现多实例共享(monostate)一个属性
class MyClass:
    _class_variable = None

    def __init__(self, var):
        self.get_variable = var

    @property
    def get_variable(self):
        return self.__class__._class_variable

    # 描述器
    @get_variable.setter
    def get_variable(self, var):
        self.__class__._class_variable = var

    def display(self):
        return self.get_variable


c1 = MyClass(1)
c2 = MyClass(2)
c2.get_variable = 3

print(c1.display())
print(c2.display())


# NOTE: 结构型模式
#  最实用的是适配模式，通常用来解决兼容问题
class UsbTypeA(object):
    def get_name(self):
        return 'TypeA 接口'

    def oneFace(self):
        return "单面"


class UsbTypeC(object):
    def get_name(self):
        return "TypeC 接口"

    def twoFace(self):
        return "双面"


class Adapter(UsbTypeC):
    def oneFace(self):
        return self.twoFace()


iface1 = UsbTypeA()
print(iface1.oneFace())
iface2 = UsbTypeC()
print(iface2.twoFace())

# NOTE: 行为模式
#  责任链模式实现了发送者和接收者解耦，让多个对象接收发送者请求，并沿着链式结构一直传递，直到由目标对象处理该请求为止
