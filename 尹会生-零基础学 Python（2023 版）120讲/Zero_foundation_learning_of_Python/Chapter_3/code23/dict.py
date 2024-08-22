# NOTE: 映射与字典

# NOTE:
#  映射是可变类型
#  映射只有一种数据类型，即：字典
#  字典里的一个元素由键和值两部分组成
#  键不能重复，因此无法哈希的类型，如列表、字典等，不可作为键来使用
#  整数1和浮点数1.0会被当作相同的键

# NOTE: 字典的定义
#  使用花括号定义：{"one":1,"two":2,"three":3}
#  使用类型构造器：dict(one =1,two=2,three=3)
#  使用字典推导式：{x:x**2 for x in range(1,11)}

# NOTE: 字典的删除
#  使用del可以删除字典
#  使用del字典[键]可以删除字典中的指定元素

list_name = ["name1", "name2", "name3"]
list_sn = [1111, 2222, 3333]
name_sn = {list_name[0]: list_sn[0], list_name[1]: list_sn[1], list_name[2]: list_sn[2]}
print(name_sn)

# NOTE: 访问字典里的内容
print(name_sn.items())
print(name_sn.values())
print(name_sn.keys())

# NOTE: 访问字典里特定的值
print(name_sn.get("name1"))

# NOTE: 遍历字典
for name, number in name_sn.items():
    print(name, number)

# NOTE: 字典默认值
default = name_sn.setdefault("toms", "default")
print(default)
print(name_sn)

# NOTE: 修改字典的内容
name_sn['name4'] = '4444'
print(name_sn)

# NOTE: 删除字典的内容
name_sn.popitem()
print(name_sn)
name_sn.pop("name1")
print(name_sn)

# NOTE: 字典的高级用法
#  如果字典存在键key，返回它对应的值
#  如果不存在，插入default的键key，并返回default 字典.setdefault(key[,default])
print(name_sn["toms"])
name_sn["toms"] = "777"
print(name_sn["toms"])
print(name_sn)

# NOTE: 用新字典的“键”和“值”更新旧的字典，新字典的“键”和“值”优先
new_name_sn = {list_name[0]: list_sn[0], list_name[1]: list_sn[1], list_name[2]: list_sn[2]}
name_sn |= new_name_sn
print(name_sn)

# NOTE: 字典与其他数据类型的混合使用
#  利用zip()函数合并两个列表为字典
zip_name_sn = dict(zip(list_name, list_sn))
print(zip_name_sn)
