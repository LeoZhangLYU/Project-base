package chapter2.code54.supermarket;

public class MerchandiseV2 {

    /**
     * 新需求：有了论斤卖的商品，数量变成double类型。有论整个卖的，有散装称重卖的，事情开始复杂起来
     */
    public String name;
    public String id;
    //    TODO 把count改成double，兼容散装称重的商品
    public int count;
    public double soldPrice;
    public double purchasePrice;

    public void init(String name, String id, int count, double soldPrice, double purchasePrice) {
        this.name = name;
        this.id = id;
        this.count = count;
        this.soldPrice = soldPrice;
        this.purchasePrice = purchasePrice;
    }

    public void describe() {
        System.out.println("商品名字叫做" + this.name + "，id是" + this.id + "。 商品售价是" + this.soldPrice + "。商品进价是" + this.purchasePrice + "。商品库存量是" + this.count + "，销售一个的毛利润是" + (this.soldPrice - this.purchasePrice));
    }

    public double calculateProfit() {
        return this.soldPrice + this.purchasePrice;
    }

    // >> TODO 方法调用的时候，参数就不必完全类型一样，实参数可以自动类型转换成形参类型即可
    public double buyDouble(double count) {
        System.out.println("bugDouble(double)被调用了");
        if (this.count < count) {
            return -1;
        }
        this.count -= count;
        double totalCost = count * soldPrice;
        return totalCost;
    }

    // >> TODO 论斤卖的商品，数量是double。我们把count成员变量改成double类型
    public double buy(double count) {
        System.out.println("buy(double)被调用了");
        if (this.count < count) {
            return -1;
        }
        this.count -= count;
        double totalCost = count * soldPrice;
        return totalCost;
    }
 
    public double buy() {
        System.out.println("buy()被调用了");
        return buy(1);
    }
}
