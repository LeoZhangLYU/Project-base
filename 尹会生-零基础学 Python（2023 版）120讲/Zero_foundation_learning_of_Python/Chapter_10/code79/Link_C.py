# NOTE: 实现混合编程的方式
#  1.使用ctypes库加载C++编写的动态链接库
#  参考链接: https://docs.python.org/zh-cn/3.10/library/ctypes.html
#  2. 使用pybind将C++编译为Python库
#  参考链接: https://github.com/pybind/python_example
#  3. 使用Pythran库将Python直接转换为C++代码
#  参考链接: https://pypi.org/project/pythran

# pythran export my_function(int list)
def my_function(arr):
    return [x * 2 for x in arr]
