# NOTE: 不定长参数:*接收位置参数；**接收关键字参数

def address_book(name, *telephone, alias_name=None, **custom):
    """

    :param name: 这是一个普通的必选参数，必须传递一个值
    :param telephone: 通过关键字传递，如果不传则使用默认值 None
    :param alias_name: 这是一个可变位置参数，允许传递任意数量的位置参数。这些参数会被收集成一个元组 (tuple)。
    :param custom: 可以传递任意数量的关键字参数，这些参数会以字典的形式接收。
    :return:
    """
    print(f"name:{name},telephone:{telephone},alias_name:{alias_name},custom:{custom}")


address_book("wilson")
address_book("wilson", 123, 456, 789)
address_book("wilson", 123, 456, 789, home="Guangdong")
address_book("wilson", 123, 456, 789, alias_name="w", home="Guangdong")
address_book("wilson", 123, 456, 789, alias_name="w", home="Guangdong", hair_color="red")


# NOTE: 不定长参数的变种:*号之后没有变量名称，只处理第一个和最后一个参数，第二个参数忽略
#  注意：由于最后一个是关键字参数，所以参数长度被固定为3个
def address_book_1(name, *, alias_name):
    pass


address_book_1("wilson", alias_name="w")

# NOTE: 函数内省
#  函数内部有很多内置的属性，这些属性是在将一个函数定义为函数对象后，自动产生的
#  你学过的默认数字类型也可以使用dir(函数)查看其内部定义的属性和方法，这些属性和方法有很多熟悉的名字，都是我们学过的数据类型默认方法
print(address_book.__doc__)
print(dir(address_book_1))
print(dir(int))
