# NOTE: 扩展数据类型
from collections import namedtuple, UserDict

# NOTE: 命名元组
#  namedtuple()是命名元组的工厂函数
#  命名元组使用前需要导入collections库
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(11, 22)
print(p1)


class Point(Point):
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p2D_1 = Point(1, 2)
p2D_2 = Point(2, 1)
print(p2D_1 + p2D_2)


# NOTE: deque双端队列
#  deque对象是实现双向队列的对象
#  双向队列能够支持从左右两端实现元素的添加和移除
#  deque比传统的列表多了appendleft(),popleft()方法

# NOTE: 计数器Counter对象
#  计数器工具可以用来统计字典中元素的数量，也可以用来统计元素的出现次数

# NOTE: 字典和列表子类化
#  UserDict类用于字典对象的二次开发
#  UserList类用于列表对象的二次开发
class MyDict(UserDict):
    def __setitem__(self, key, value):
        if key in self.keys():
            print(f"字典里已经有key {key}，不能添加/覆盖")
        else:
            self.data[key] = value


dict1 = MyDict()
dict1['x'] = 1
dict1['x'] = 2
