# 复数
x = 1 + 2im
println("Complex Number: ", x, " of type ", typeof(x))

println("Real Part: ", real(x)) # 取实部
println("Imaginary Part: ", imag(x)) # 取虚部
println("Conjugate: ", conj(x)) # 共轭复数
println("Magnitude: ", abs(x)) # 复数的模
println("abs2: ", abs2(x)) # 复数模的平方
println("Angle (radians): ", angle(x)) # 复数的幅角（弧度）

a = 1
b = 2
z = complex(a, b) # 创建复数
println("Complex from real and imag: ", z)

# 有理数:如果一个分数的分子和分母含有公因子，它们会被约分到最简形式且分母非负
y = 6 // 8
println("Rational Number: ", y, " of type ", typeof(y))
println("Numerator: ", numerator(y)) # 分子
println("Denominator: ", denominator(y)) # 分母
# 分数转浮点数
println("Float value: ", float(y))