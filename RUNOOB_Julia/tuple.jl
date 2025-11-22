# 元组命名
name_shape = (:corner, :edge, :face, :body)
value_shape = ((0, 0), (0, 1), (1, 1), (1, 1, 1))
shapes = NamedTuple{name_shape}(value_shape)
println("Named Tuple of Shapes: ", shapes)
println("Access corner: ", shapes.corner)

# 键(key)和值(value)同时在一个元组中
shape_item = (corner1 = (1, 1), corner2 = (-1, -1), center = (0, 0))
println("Shape Item Tuple: ", shape_item)
println("Access center: ", shape_item.center)

# 合并两个已命名的元组
merged_shapes = merge(shapes, shape_item)
println("Merged Shapes Tuple: ", merged_shapes)

# 元组解包作为函数参数
function testFunc(x, y, z; a=10, b=20, c=30)
    println("x = $x, y = $y, z = $z; a = $a, b = $b, c = $c")
end
# 创建元组
options = (b = 200, c = 300)
# 执行函数，元组作为参数传入
testFunc(1, 2, 3; options...)

# 元组解包与参数覆盖
function testFunc(x, y, z; a=10, b=20, c=30)
    println("x = $x, y = $y, z = $z; a = $a, b = $b, c = $c")
end
# 创建元组
options = (b = 200, c = 300)
# 执行函数，元组作为参数传入，指定参数在元组前，不会覆盖
testFunc(1, 2, 3; b = 1000000, options...)
# 执行函数，元组作为参数传入，指定参数在元组后，会覆盖
testFunc(1, 2, 3; options..., b= 1000000)

# NOTE: 在Julia中1000000和1000_000是等价的，均表示一百万。下划线仅用于提高数字的可读性，不影响数值本身。

# 元组解包
point = (3, 4, 5)
(x, y, z) = point
println("Unpacked Point: x = $x, y = $y, z = $z")

