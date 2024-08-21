# NOTE: 添加元素
#  list.insert（索引，元素）在索引位置插入元素
#  list.append（元素）在列表结尾添加元素
#  list.extend（可迭代对象*）为列表扩展元素
#  ⭐append 和 extend 参数为列表时，增加的结果不同
list_demo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', ['h', 'i', 'j']]
print(list_demo)
print(type(list_demo))
list_demo.insert(0, 'first')
list_demo.insert(-1, 'first')  # -1表示最后一个元素，但是insert()永远不能在最后插入
print(list_demo)
list_demo.append('last')
print(list_demo)
list_demo.extend('last')
print(list_demo)

# NOTE: 修改元素
#  list.remove(元素)移除列表的元素
#  list.reverse()反转列表元素的顺序
#  list.pop（索引）移除索引对应的元素并返回该元素，不指定索引移除最后一个元素
#  list.copy()复制列表
#  list.clear()清空列表
list_demo.remove('a')
print(list_demo)
list_demo.reverse()
print(list_demo)
pop = list_demo.pop(0)
print(list_demo)
print(pop)
list_demo.pop()
print(list_demo)

# NOTE: 计算列表长度
#  len（list）得到列表的长度
#  len（list[0]）得到列表中元素的长度
#  list.count（元素）元素出现的次数

# NOTE: 列表排序
#  list.sort(reverse=True)列表原地排序
#  sort（list）列表排序后返回新的列表
