# 文件读写
path_txt = joinpath(@__DIR__, "file_operation", "example.txt") # joinpath会自动处理不同操作系统的路径分隔符
# 在Julia中，建议使用 do 语法来处理文件读写操作，以确保文件在操作完成后正确关闭
open(path_txt, "w") do io
    write(io, "Hello, Julia!\n")
    write(io, "This is a file operation example.\n")
end

# 读取文件内容
open(path_txt, "r") do io
    content = read(io, String)
    println("文件内容:\n", content)
end
# readline() 函数逐行读取文件
open(path_txt, "r") do io
    println("逐行读取文件内容:")
    while !eof(io)
        line = readline(io)
        println(line)
    end
end
# eachline() 函数逐行读取文件
open(path_txt, "r") do io
    println("使用 eachline() 逐行读取文件内容:")
    for line in eachline(io)
        println(line)
    end
end

# 文件的信息
file_info = stat(path_txt)
println("文件信息:", file_info)

# 绝对路径
absolute_path = abspath(path_txt)
println("文件绝对路径: ", absolute_path)