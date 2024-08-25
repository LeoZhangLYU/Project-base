# NOTE: 列表类型的特殊性
#  列表是可变数据类型
#  元组的元素可以是列表
#  可变类型，作为函数的参数，导致数据处理时发生变化

list1 = ["x", "y", "z"]
tuple1 = (list1, "b", "c")
tuple1[0][0] = "abc"
print(tuple1)
print(list1)
