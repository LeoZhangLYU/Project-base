# NOTE: F-strings介绍
#  F-strings是3.6新增的字符串格式化功能
#  比百分号和str.format()更友好
#  采用了早期为字符串添加关键字方式，如"u","r","b"

# NOTE: F-strings的计算功能
#  F-strings的{}中可以实现数字计算、字符串连接、函数执行等计算任务
#  嵌入的内容可解释执行
#  f"{1 +2}"

# NOTE: 宽度和精度调整格式
#  f"{对象：宽度.精度类型}"   类型同百分号格式化输出
number = 123.456
print(f'{number:10}')
print(f'{number:<10}')
print(f'{number:010}')
print(f'{number:4f}')  # 指定类型后，默认保存小数点后6位
print(f'{number:.10f}')  # 指定类型后，默认保存小数点后6位
