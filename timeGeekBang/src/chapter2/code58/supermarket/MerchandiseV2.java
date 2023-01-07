package chapter2.code58.supermarket;

public class MerchandiseV2 {

    // 静态变量使用static修饰符
    public static double DISCOUNT_FOR_VIP = 0.95;
    public String name;
    public String id;
    public int count;
    public double soldPrice;
    public double purchasePrice;

    public MerchandiseV2(String name, String id, int count, double soldPrice, double purchasePrice) {
        this.name = name;
        this.id = id;
        this.count = count;
        this.soldPrice = soldPrice;
        this.purchasePrice = purchasePrice;
    }

    // >> TODO 静态方法使用 static 修饰符
    //    TODO 静态方法的方法名没有约定俗成全大写
    public static double getVIPDiscount() {
        // >> TODO 静态方法可以访问静态变量，包括自己类的静态变量和在访问控制符允许的别的类的静态变量
        return DISCOUNT_FOR_VIP;
    }

    // >> TODO 除了没有this，静态方法的定义和成员方法一样，也有方法名，返回值和参数。
    // >> TODO 静态变量没有this自引用，它不属于某个实例，调用的时候也无需引用，直接用类名调用，所以它也不能直接访问成员变量
    // >> TODO 当然，在静态方法里面，也可以自己创建对象，或者通过参数，获得对象的引用，进而调用方法和访问成员变量
    // >> TODO 静态方法只是没有this自引用的方法而已
    public static double getDiscountOnDiscount(LittleSuperMarket littleSuperMarket) {
        double activityDiscount = littleSuperMarket.activityDiscount;
        return DISCOUNT_FOR_VIP * activityDiscount;
    }

    public String getName() {
        return name;
    }

    public void describe() {
        System.out.println("商品名字叫做" + name + "，id是" + id + "。 商品售价是" + soldPrice
                + "。商品进价是" + purchasePrice + "。商品库存量是" + count +
                "。销售一个的毛利润是" + (soldPrice - purchasePrice));
    }

    public double calculateProfit() {
        double profit = soldPrice - purchasePrice;
        return profit;
    }
}
