package chapter2.code43.supermarket;

public class MerchandiseV2 {

    /**
     * 名字
     */
    public String name;
    public String id;

    /**
     * 数量
     */
    public int count;

    /**
     * 售价
     */
    public double soldPrice;

    /**
     * 进价
     */
    public double purchasePrice;

    /**
     * 产地
     */
    public String madeIn;

    // >> TODO 访问修饰符
    // >> TODO 返回值类型：无需返回值则用void表示，void是java中的关键字
    // >> TODO 方法名：任意合法的标识符都可以
    // >> TODO 参数列表：后续讲解
    // >> TODO 方法体：方法的代码
    // >> TODO 方法体定义的变脸叫
    public void describe() {
        System.out.println(
            "商品名字叫做" + name + "，id是" + id + "。 商品售价是" + soldPrice + "。商品进价是"
                + purchasePrice + "。商品库存量是" + count + "。销售一个的毛利润是" + (soldPrice
                - purchasePrice) + "。生产地址为：" + madeIn);
    }

}
