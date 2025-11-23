# 数学函数
x = NaN
y = 100
z = Inf
# x与y的值与类型是否完全相同
println("x and y are identical: ", isequal(x, y))
# 是否是有限大的数字
println("y is finite: ", isfinite(y))
println("z is finite: ", isfinite(z))
# 是否是无穷大
println("z is infinite: ", isinf(z))
# 是否是NaN
println("x is NaN: ", isnan(x))

# NOTE: isequal与==的区别在于，isequal会将NaN视为相等，而==不会
println("x == x: ", x == x)
println("isequal(x, x): ", isequal(x, x))
# NOTE: isequal还会区分+0.0和-0.0，而==不会
println("+0.0 == -0.0: ", +0.0 == -0.0)
println("isequal(+0.0, -0.0): ", isequal(+0.0, -0.0))

# 舍入函数
a = 3.8
# 舍到最接近的整数
println("round(3.8) = ", round(a))
println("round(Int16, 3.8) = ", round(Int16, a))
# 向下取整,	x 向 -Inf 舍入
println("floor(3.8) = ", floor(a))
println("floor(Int16, 3.8) = ", floor(Int16, a))
# 向上取整,	x 向 +Inf 舍入
println("ceil(3.8) = ", ceil(a))
println("ceil(Int16, 3.8) = ", ceil(Int16, a))
# 截断,	x 向零舍入
println("trunc(3.8) = ", trunc(a))
println("trunc(Int16, 3.8) = ", trunc(Int16, a))

# 除法函数
# alpha和beta......的最大公约数
alpha = 54
beta = 24
println("gcd(54, 24) = ", gcd(alpha, beta))
# alpha和beta......的最小公倍数
println("lcm(54, 24) = ", lcm(alpha, beta))

# 符号和绝对值函数
b = -42
println("sign(-42) = ", sign(b)) # 符号函数
println("abs(-42) = ", abs(b))   # 绝对值函数
println("abs2(-42) = ", abs2(b)) # 绝对值的平方
println("signbit(-42) = ", signbit(b)) # 是否为负数
println("copysign(3.5, -42) = ", copysign(3.5, b)) # 将3.5的符号改为-42的符号
println("sqrt(49) = ", sqrt(49)) # 平方根
println("cbrt(27) = ", cbrt(27)) # 立方根
println("当直角边的长度为 x 和 y时，直角三角形斜边的长度 hypot(3, 4) = ", hypot(3, 4)) # 计算sqrt(x^2 + y^2)
println("exp(1) = ", exp(1)) # e的指数函数
println("log(e) = ", log(exp(1))) # 自然对数
println("log10(1000) = ", log10(1000)) # 以10为底的对数
println("log2(1024) = ", log2(1024)) # 以2为底的对数

# 三角和双曲函数
angle = π / 4 # 45度，弧度制
println("sin(π/4) = ", sin(angle)) # 正弦函数
println("cos(π/4) = ", cos(angle)) # 余弦函数
println("tan(π/4) = ", tan(angle)) # 正切函数