package chapter2.code61.supermarket;

// >> TODO 类，静态方法，静态变量，成员变量，构造方法，成员方法都可以使用访问修饰符
public class MerchandiseV2 {

    public static double DISCOUNT = 0.1;
    // >> TODO 成员变量应该都声明为private
    // >> TODO 如果要读写这些成员变量，最好用get set方法，这些方法应该是public的
    // >> TODO 这样做的好处是，如果有需要，可以通过代码，检查每个属性值是否合法
    private String name;
    private String id;
    private int count;
    private double soldPrice;
    private double purchasePrice;
    private NonPublicClassCanUserAnyName nonPublicClassCanUserAnyName;

    // >> TODO 构造方法如果是private的，那么就只有当前的类可以调用这个构造方法
    private MerchandiseV2(String name, String id, int count, double soldPrice, double purchasePrice) {
        this.name = name;
        this.id = id;
        this.count = count;
        this.soldPrice = soldPrice;
        this.purchasePrice = purchasePrice;
    }

    // >> TODO 有些时候，会把所有的构造方法都定义成private的，然后使用静态方法调用构造方法
    // >> TODO 同样的，这样的好处是可以通过代码，检查每个属性值是否合法
    private static MerchandiseV2 createMerchandise(String name, String id, int count, double soldPrice,
                                                   double purchasePrice) {
        if (soldPrice < 0 || purchasePrice < 0) {
            return null;
        }
        return new MerchandiseV2(name, id, count, soldPrice, purchasePrice);
    }

    public MerchandiseV2(String name,String id,int count,double soldPrice){
        this(name,id,count,soldPrice,soldPrice*0.8);
    }

    public MerchandiseV2(){
        this("无名","000",0,1,1.1);
    }

}
