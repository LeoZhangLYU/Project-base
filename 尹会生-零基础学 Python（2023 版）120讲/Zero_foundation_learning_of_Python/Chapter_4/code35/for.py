# NOTE: for循环与while循环的区别
#  for语句和while语句都能实现循环处理逻辑
#  for语句更多用于对象的遍历，即：将对象中的每个元素挨个操作一遍
#  for语句对对象进行遍历：for 存储对象元素的变量 in 对象
#  直到条件不满足或每个元素都被处理（术语：迭代）完成，for循环结束
for temp_element in (1, 2, 3, 4):
    print(temp_element)

friends = ["wilson", "monica", "john", "wang"]
for friend in friends:
    print(friend.capitalize())

movie1 = {"name": "Friends", "language": "English", "Sessions": 10, "Other name": "Six of one"}
for value in movie1.values():
    print(f"{value}")
for i, value in enumerate(movie1.items()):
    print(f"{i}: {value}")

# NOTE: 推导式案例
print([i for i in movie1.values()])
print([i for i in movie1.values() if type(i).__name__ == 'int'])

# NOTE: 总结
#  for循环通常用于遍历列表、元组、字典
#  通过迭代，for循环可以实现对对象中的每个元素进行单独处理
#  为了便于迭代时进行数量计算，可以引入枚举函数enumerate(),将对象转换为元组，再利用元组解包方式快速提取每个元素的编号
