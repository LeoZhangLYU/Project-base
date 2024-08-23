# NOTE: while循环语法
number = 1
while number <= 10:
    print(f"number is {number}")
    number += 1

# NOTE: 循环的退出情况：

# 循环结束，正常退出
# 执行出错，异常退出
# 使用标志退出
number = 10
while number >= 1:
    print(f"number is {number}")
    number -= 1
    if number == 5:
        break
        # continue
# 使用break、continue语句退出
# 条件不满足，不执行循环
# 死循环，不退出

# NOTE: 使用while循环操作列表
list1 = []
number = 1
while number <= 10:
    list1.append(number)
    number += 1
print(list1)

# NOTE: 使用while循环遍历列表
while list1:
    print(list1.pop())
