# 各种除法
x = 7 / 8
y = div(7, 8) # 整除
z = fld(7, 8) # 向下取整除
r = 7 % 8 # 取余
m = mod(7, 8) # 取模
println("7 / 8 = ", x, " of type ", typeof(x))
println("div(7, 8) = ", y, " of type ", typeof(y))
println("fld(7, 8) = ", z, " of type ", typeof(z))
println("7 % 8 = ", r, " of type ", typeof(r))
println("mod(7, 8) = ", m, " of type ", typeof(m))

# 链式比较:注意比较执行顺序
compare = 1 < 2 <= 2 < 3 == 3 > 2 >= 1 == 1 < 3 != 5
println("Chained comparison result: ", compare)
M(a) = (println(a); a)
compare_chain = M(1) < M(2) <= M(3)
println("Chained comparison with side effects result: ", compare_chain)
compare_chain_2 = M(1) > M(2) <= M(3)
println("Chained comparison with side effects result: ", compare_chain_2)

# 位运算
a = 123 # 二进制表示的整数12
b = 234 # 二进制表示的整数10
println("按位取反a = ", ~a, ",按位取反b = ", ~b)
println("按位与 a & b = ", a & b)
println("按位或 a | b = ", a | b)
println("按位异或 a ⊻ b = ", xor(a, b))
println("按位非与 a ⊼ b = ", ~(123 & 123))
println("按位非或 a ⊽ b = ", ~(123 | 124))

# 向量化 "点" 运算符
v1 = [1, 2, 3]
println("v1 = ", v1 .* 2) # 向量化平方