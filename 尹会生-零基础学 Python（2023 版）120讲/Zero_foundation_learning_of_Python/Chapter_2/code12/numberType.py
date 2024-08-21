# TODO: Python是强类型编程语言
"""
    数字类型种类：整数、浮点数和复数
    使用type()函数可以得知对象的类型
    int()、float()函数可以进行数字之间类型之间的转换
    str()函数能够将数字转换为字符串
    int()函数可以将只含有整数的字符串转换为整数，否则报错
"""
print(int(123.324))

Total = 0
for item in [1, 2]:
    x = input(f"请输入第{item}个值：")
    Total += int(x)
print(Total)
