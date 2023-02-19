package chapter2.code68.supermarket;

// >> TODO 继承的语法就是在类名后面使用extends加要继承的类名
// >> TODO 被继承的类叫做父类（parent class），比如本例中的MerchandiseV2
// >> TODO 继承者叫做子类（sub class），比如本例中的PhoneExtendsMerchandise
// >> TODO java中只允许一个类有一个直接的父类，（parent class），即所谓的单继承
// >> TODO 没错，别的类也可以继承子类，比如可以有一个HuaweiPhone继承PhoneExtendsMerchandise
//    TODO 这时候，HuaweiPhone就是PhoneExtendsMerchandise的子类了
// >> TODO 子类继承了父类什么呢？所有的方法和属性。
// >> TODO 但是子类并不能访问父类的private的成员（包括方法和属性）

public class PhoneExtendsMerchandise extends MerchandiseV2 {

    // 给Phone增加新的方法和属性
    private double screenSize;
    private double cpuHZ;
    private int memoryG;
    private int storageG;
    private String brand;
    private String os;

    public PhoneExtendsMerchandise(String name, String id, int count, double soldPrice, double purchasePrice,
                                   double screenSize, double cpuHZ, int memoryG, int storageG, String brand,
                                   String os) {
        this.screenSize = screenSize;
        this.cpuHZ = cpuHZ;
        this.memoryG = memoryG;
        this.storageG = storageG;
        this.brand = brand;
        this.os = os;

        this.setName(name);
        this.setId(id);
        this.setCount(count);
        this.setSoldPrice(soldPrice);
        this.setPurchasePrice(purchasePrice);
    }

    public void descibutePhone() {
        System.out.println("此手机商品属性如下：");
        describe();
        System.out.println("手机厂商为" + brand + "；系统为" + os + "；硬件配置如下：\n" + "屏幕：" + screenSize + "寸\n" + "cpu主频" + cpuHZ + " GHz\n" + "内存" + memoryG + "Gb\n" + "存储空间" + storageG + "Gb\n");
    }

    public boolean meetCondition() {
        return true;
    }

}
