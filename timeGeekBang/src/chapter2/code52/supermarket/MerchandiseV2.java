package chapter2.code52.supermarket;

public class MerchandiseV2 {

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
}
