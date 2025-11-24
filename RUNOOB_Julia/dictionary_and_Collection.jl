# 字典和集合
first_dict = Dict(string(i) => i^2 for i in 1:5)
println("字典内容: ", first_dict)
println("访问字典元素 first_dict[\"3\"] = ", first_dict["3"])

# 添加和修改字典元素
first_dict["6"] = 36
println("添加元素后字典内容: ", first_dict)
# 字典中的键是唯一的，如果我们为一个已经存在的键分配一个值，我们不会创建一个新的，而是修改现有的键。
first_dict["2"] = 20
println("修改元素后字典内容: ", first_dict)
# 删除字典元素
delete!(first_dict, "4")
println("删除元素后字典内容: ", first_dict)

# 查找
println("检查键 \"5\" 是否存在: ", haskey(first_dict, "5"))
println("获取所有键: ", keys(first_dict))
println("获取所有值: ", values(first_dict))
# in() 函数可以用来检查某个键值对是否存在于字典中
println("检查键 \"'1' => 1\" 是否存在: ", ("1" => 1) in first_dict)

# 排序:使用 DataStructures.ji 包中的 SortedDict 数据类型让字典始终保持排序状态
using DataStructures
sorted_dict = SortedDict(first_dict)
println("排序后的字典内容: ", sorted_dict)

# 集合
first_set = Set([1, 2, 3, 4, 5])
println("集合内容: ", first_set)
# 添加元素
push!(first_set, 6)
println("添加元素后集合内容: ", first_set)
# 删除元素
delete!(first_set, 3)
println("删除元素后集合内容: ", first_set)
# 查找
println("检查元素 4 是否存在: ", in(4, first_set))


# 并集
second_set = Set([4, 5, 6, 7, 8])
union_set = union(first_set, second_set)
println("集合并集: ", union_set)
# 交集
intersection_set = intersect(first_set, second_set)
println("集合交集: ", intersection_set)
# 差集
difference_set = setdiff(first_set, second_set)
println("集合差集: ", difference_set)