# 流程控制语句

# 复合表达式 begin...end
x = begin
    a = 1
    b = 2
    a + b
end
println("复合表达式结果: ", x)

# 条件语句 if...elseif...else
y = 10
if y < 0
    println("y 是负数")
elseif y == 0
    println("y 是零")
else
    println("y 是正数")
end
# 三元运算符
z = y > 5 ? "大于5" : "不大于5"
println("三元运算符结果: ", z)

# 短路运算 && 和 ||，&& 优先级高于 ||
a = 5
b = 0
# b /= a 只有在 a > 0 为 true 时才会执行
println("短路与运算结果: ", (a > 0) && (b /= a), ", b = ", b)
# b += a 只有在 a < 0 为 false 时才会执行
println("短路或运算结果: ", (a < 0) || (b += a), ", b = ", b)

# 循环语句 for...in 和 while
println("for 循环输出:")
for i in 1:5
    println("i = ", i)
end
println("while 循环输出:")
# NOTE: Julia 中没有 do...while 循环
index = 1
while index <= 5
    global index # 使用 global 关键字修改外部变量
    println("index = ", index)
    index += 1
end


# 循环控制语句 break 和 continue
println("使用 break 退出循环:")
for i in 1:10
    if i == 6
        println("i 等于 6，退出循环")
        break
    end
    println("i = ", i)
end
println("使用 continue 跳过当前迭代:")
for i in 1:10
    if i % 2 == 0
        println("i 等于 ", i, "，是偶数，跳过")
        continue
    end
    println("i = ", i)
end

# 标签语句
println("使用标签语句控制嵌套循环:")

function demo_label()
    for i in 1:3
        for j in 1:3
            if i == 2 && j == 2
                println("i 和 j 都等于 2，跳出外层循环")
                @goto outer_end        # 跳到标签 outer_end
            end
            println("i = ", i, ", j = ", j)
        end
    end

    @label outer_end                    # 标签定义在同一个函数作用域里
end

demo_label()

# 异常处理 try...catch...finally
println("异常处理示例:")
function demo_exception_handling()
    try
        println("尝试除以零")
        result = 10 / 0
        println("结果: ", result)
    catch e
        println("捕获到异常: ", e)
    finally
        println("执行 finally 块")
    end
end

demo_exception_handling()

# throw 和 catch
println("自定义异常示例:")
struct MyError <: Exception
    msg::String
end
function demo_custom_exception()
    try
        println("抛出自定义异常")
        throw(MyError("这是一个自定义异常"))
    catch e
        if e isa MyError
            println("捕获到自定义异常: ", e.msg)
        else
            println("捕获到其他异常: ", e)
        end
    end
end

demo_custom_exception()