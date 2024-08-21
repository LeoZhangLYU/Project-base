# NOTE:
#  列表中可以存放一系列对象
#  存放的对象可以是数字、字符串、列表
#  列表用方括号[]表示，每个对象称作列表的元素，元素之间使用“，”分割
#  列表中的元素可以在定义列表之后进行修改，也可以使用索引来访问一个或多个元素
#  列表也支持了丰富的内置函数

list1 = [1, 2, 3, 4, 5]
list2 = ['aa', 'cc', 'dd']
list3 = [123, 'abc']
list4 = [[1, 'a'], [2, 'b', 'c'], [3, 'd']]

colors = ['red', 'green', 'blue']
print(colors)
print(type(colors))

# NOTE: 使用内置函数list()也可以将字符串创建为列表
list5 = list("red")
print(list5)

# NOTE: 使用列表推导式创建列表
list6 = [x for x in range(1, 10)]
print(list6)

# NOTE: 访问列表的元素：列表是有序的数据类型，可以通过索引访问到列表的每一个元素
print(list3[1])
print(list4[1][2])

# NOTE: 删除列表的元素和删除列表
del list2[1]
del list3
