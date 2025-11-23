# 字符串
# NOTE: Julia中的字符串是不可变的UTF-8编码的字符序列
x = "Hello, "
y = "World!"
println("Concatenation: ", x * y) # 字符串连接
println("Concatenation using string(): ", string(x, y)) # 使用string函数连接字符串
println("Repetition: ", x^3)    # 字符串重复
println("Length of x: ", length(x)) # 字符串长度
println("Character at index 8 of y: ", y[5], " type:", typeof(y[5])) # 访问字符串中的字符
println("Substring of y from index 5 to 5: ", y[5:5], " type:", typeof(y[1:5])) # 子字符串

# 查找
substr = "l"
index = findfirst(substr, x)
println("Index of substring 'l' in x: ", index)
indices = findall(substr, x)
println("All indices of substring 'l' in x: ", indices)
next_index = findnext(substr, x, last(index) + 1)
println("Next index of substring 'l' in x after index ", index, ": ", next_index)
last_index = findlast(substr, x)
println("Last index of substring 'l' in x: ", last_index)
# 检查包含
pattern = "or"
println("Does y contain 'or'? ", occursin(pattern, y))
# 检查开头和结尾
println("Does x start with 'He'? ", startswith(x, "He"))
println("Does y end with 'd!'? ", endswith(y, "d!"))
# nextind 和 prevind: 用于处理多字节字符串中的索引,查找下一个和上一个字符的索引,(str,i,n)表示从索引i开始，跳过n个字符后的索引
s = "Hello, 世界!"
i = firstindex(s)
println("First index: ", i)
next_i = nextind(s, i, 7)
println("Next index: ", next_i)
prev_i = prevind(s, next_i, 7)
println("Previous index: ", prev_i)

# 替换
original = "Hello, World!"
replaced = replace(original, "World" => "Julia")
println("Original string: ", original)
println("Replaced string: ", replaced)

# 分割
csv = "apple,banana,cherry"
fruits = split(csv, ",")
println("Fruits: ", fruits)


