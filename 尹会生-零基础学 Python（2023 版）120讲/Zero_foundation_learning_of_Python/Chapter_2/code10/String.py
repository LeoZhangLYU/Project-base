x = 123
print("x的值为{}".format(x))
print(f"x的值为{x}")

# 字符串的基本操作
# TODO: 成员运算
print("x" in "123x456")
print("x" not in "123y456")

# TODO: 连接运算
print("abc" + "xyz")
print("abc" * 3)

# TODO: 切片运算
y = "qwertyuiop"
# s[i]:第i项，起始为0
# s[i:j]:第i到j的切片，不包含j
# s[i:j:k]:从i到j步长为k的切片
print(y[3])
print(y[-1])
print(y[1:3])
print(y[1:7:2])

# TODO: 字符串的常用方法
''' 
str.count(sub[, start[, end]])
返回子字符串sub 在[start，end]范围内非重叠出现的次数

str.isalnum()
如果字符串中的所有字符都是字母或数字，且至少有一个字符，那么返回True，否则返回False

str.isalpha()
如果字符串中的所有字符都是字母，且至少有一个字符，那么返回True，否则返回False

str.join(iterable)
返回一个由iterable 中的字符串拼接而成的字符串

str.split(sep=None, maxsplit = -1)
返回一个由字符串内单词组成的列表，使用sep作为分隔字符串

str. startswith(prefix[, start[, end]])
如果字符串以指定的 prefix 开始，那么返回 True，否则返回 False
'''
print("xyz".count(y))
print("xyz".isalnum())
print("xyz".isalpha())
print(",".join(y))
print(",".join(y).split(","))
print(y.startswith("qw"))
