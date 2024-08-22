# NOTE: 集合与set对象
#  集合类型包括set和frozenset两种对象
#  set对象可变，frozenset对象不可变
#  set对象在程序设计中较常使用

# NOTE: 集合可以用多种方式创建
#  使用花括号内，以逗号分隔元素的方式{"wilson","yin"}
#  使用集合推导式
#  使用类型构造器set()
color = ("red", "green", "blue", "red", "green", "blue")
new_color = set(color)
print(new_color)
new_color2 = tuple(new_color)
print(new_color2)

# NOTE: 使用del删除set对象

# NOTE: 集合的唯一性是经常使用该数据类型的主要原因
#  从序列中去除重复项等操作，可以通过数据类型强制转化实现
