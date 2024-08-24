products = [[1000, "iphone", "phone", 12000], [1001, "ipad", "pad", 15000], [1002, "macbook", "laptop", 20000]]
cart = {1000: 5, 1001: 2}


def id_to_name(product_id):
    """
    产品id转产品名
    :param product_id:
    :return:
    """
    for i, product in enumerate(products):
        if product_id == product[0]:
            return product[1]


def id_to_price(product_id):
    """
    产品id转产品价格
    :param product_id:
    :return:
    """
    for i, product in enumerate(products):
        if product_id == product[0]:
            return product[3]


def show_cart():
    """
    展示购物车里的商品
    :return:
    """
    total_price = 0
    for i in cart:
        print(f"购买商品{id_to_name(i)}的数量为{cart[i]}")
        total_price += cart[i] * id_to_price(i)
    print(total_price)
