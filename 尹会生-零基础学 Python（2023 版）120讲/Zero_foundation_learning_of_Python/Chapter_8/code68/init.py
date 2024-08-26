import Custom_module as custom_module

print(dir(custom_module))
print(custom_module.var1)
custom_module.func1()
object1 = custom_module.Class1()

# NOTE: 自定义模块注意事项
#  导入自定义模块时，需确保导入路径正确
#  自定义模块的文件名称尽量避免特殊字符，文件名应避免和标准库重名
#  自定义模块多次导入，模块中的代码也只能被执行一次
#  自定义模块中应为函数定义，避免在模块中编写函数调用代码，或将函数调用代码放在__name__代码块中
