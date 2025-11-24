import Base.Meta

"""
    @debug_expr expr

打印表达式本身、AST（用 Meta.show_sexpr 展示）以及计算结果，
然后返回表达式的结果。
"""
macro debug_expr(ex)
    # 在宏展开阶段把 AST 打成字符串，方便在运行时打印
    ast_str = sprint(Meta.show_sexpr, ex)

    return quote
        println("表达式: ", $(string(ex)))
        println("AST   : ", $ast_str)
        result = $(esc(ex))   # 真正执行原始表达式
        println("结果  : ", result)
        result
    end
end


x = 10
y = @debug_expr x + 2 * 3
println("最终结果: ", y)