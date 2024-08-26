# NOTE: 自定义异常
class MyException(Exception):
    def __init__(self, value):
        self.message = value

    @property
    def msg(self):
        return f"名字不允许用{self.message}"


name = "jerry"
try:
    if name == "jerry":
        raise MyException(name)
except MyException as e:
    print(e.msg)


# NOTE: with语句：使用了__enter__()和__exit__()两个方法实现
class MyClass:
    def __enter__(self):
        # with语句后的对象会被调用，并将结果返回给as语句后的对象
        print("enter调用")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # with语句块所有代码执行完，执行此部分代码
        print("exit调用")


with MyClass() as mc:
    print("mc实例化")
