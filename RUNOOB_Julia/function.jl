# 函数
function add(x, y)
    return x + y
end
result = add(3, 5)
println("3 + 5 = ", result)

# 指定参数类型与返回类型
function multiply(x::Int, y::Int)::Int
    return x * y
end
result = multiply(4, 6)
println("4 * 6 = ", result)

# 可选参数函数
function greet(name::String, greeting::String="Hello")
    return "$greeting, $name !"
end
result = greet("Alice")
println(result)
result = greet("Bob", "Hi")
println(result)

# 关键字参数函数
function introduce(name::String; age::Int=0, city::String="Unknown")
    return "Name: $name, Age: $age, City: $city"
end
result = introduce("Charlie", age=30, city="New York")
println(result)

# 可变参数函数
function sum_all(nums::Int...)
    total = 0
    for num in nums
        total += num
    end
    return total
end
result = sum_all(1, 2, 3, 4, 5)
println("Sum of 1, 2, 3, 4, 5 = ", result)

# 匿名函数
square = x -> x^2
result = square(7)
println("Square of 7 = ", result)
# 高阶函数
function apply_function(f::Function, x)
    return f(x)
end
result = apply_function(square, 9)
println("Applying function to 9 = ", result)

# 函数嵌套
function outer_function(x)
    function inner_function(y)
        return y^2
    end
    return inner_function(x) + 1
end
result = outer_function(3)
println("Result of outer_function(3) = ", result)

# Map
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(x -> x^2, numbers)
println("Squared numbers: ", squared_numbers)

# Filter
even_numbers = filter(x -> x % 2 == 0, numbers)
println("Even numbers: ", even_numbers)
