package chapter2.code53.supermarket;

public class MerchandiseV2Overload {

    public String name;
    public String id;
    public int count;
    public double soldPrice;
    public double purchasePrice;

    public void init(String name, String id, int count, double soldPrice, double purchasePrice) {
        if (soldPrice < 0) {

        }
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

    // >> TODO 重载的方法可以调用别的重载方法，当然也可以调用别的不重载的方法。
    // >> TODO 实际上，像这种补充一些缺省的参数值，然后调用重载的方法，是重载的一个重要的使用场景
    // >> TODO 在这里我们举的例子就是这样的，但是不是语法要求一定要这样。重载的方法的方法体内代码可以随便调用，可以不调用别的重载方法。
    public double buy() {
        return buy(1);
    }

    public double buy(int count) {
        return buy(count, false);
    }

    //    TODO 最后都补充好参数，调用参数最全的一个方法
    public double buy(int count, boolean isVIP) {
        if (this.count < count) {
            return -1;
        }
        this.count -= count;
        double totalCost = count * soldPrice;
        if (isVIP) {
            return totalCost * 0.95;
        } else {
            return totalCost;
        }
    }
}
