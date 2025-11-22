arr = [1, 2, 3, 4, 5]
println("Array: ", arr)

arr2d = [1 "ROUND" 3.5; 4 "SQUARE" pi]
println("2D Array: ", arr2d)
println("Element at (2,3): ", arr2d[2,3])
println("Element at end:", arr2d[end])

arrInt = Int64[10, 20, 30]
println("Integer Array: ", arrInt)

arrNone = []
println("Empty Array: ", arrNone)

# 指定数组的类型和维度
ArrayType = Array{Int64}(undef, 3, 4)
println("Array with specified type and dimensions: ", typeof(ArrayType), " with size ", size(ArrayType))

# 定义行
rowArr = [1 2 3; 4 5 6]
println("Row Array: ", typeof(rowArr), " with size ", size(rowArr))
# 定义列 (1,5)
colArr = [1;; 2;; 3;; 4;; 5]
println("Column Array: ", typeof(colArr), " with size ", size(colArr))
# 定义列向量（5,）
colVec = [1;2;3;4;5]
println("Column Vector: ", typeof(colVec), " with size ", size(colVec))

# 也可以在方括号 [] 中嵌入多个长度相同的一维数组，并用空格分隔来创建二维数组
arrFromRows = [[1;2] [3;4] [5;6]]
println("Array arrFromRows", arrFromRows)
println("Array from rows: ", typeof(arrFromRows), " with size ", size(arrFromRows))

# 使用 range 创建数组
rangeArr = collect(Float64,range(1, stop=10, step=2))
println("Range Array: ", rangeArr)

# 使用推导式和生成器创建数组
compArr = [x^2 for x in 1:5]
println("Comprehension Array: ", compArr)
# 创建二维数组
compArr2d = [i + j for i in 1:3, j in 1:3]
println("2D Comprehension Array: ", compArr2d, " with size ", size(compArr2d))

using LinearAlgebra
# m 行 n 列的单位矩阵 （需要先执行 using LinearAlgebra 来才能使用 I）
identityMat = Matrix{Float64}(I, 3, 3)
println("Identity Matrix: ", identityMat)

# 用值 x 填充数组 A
A = zeros(3, 4)
filledArr = fill!(A, 7)
println("Filled Array: ", filledArr)
# 一个被值 x 填充的 Array
filledArr2 = fill(9, 2, 5)
println("Filled Array 2: ", filledArr2)

