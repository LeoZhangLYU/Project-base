package chapter2.code69.supermarket;
// >> TODO 继承，其实表达的是一种“is-a”的关系，也就是说，在你用类构造的世界中，“子类是父类的一种特殊类别“

// >> TODO 继承和组合，是拿到一个问题，设计相应的java类的时候，不得不面对的来自灵魂的拷问。
//    TODO ”XX到底是YY的一种，还只是组合了YY？“，”手机到底是手电筒的一种，还是组合了一个可以当手电的闪光灯？“

// >> TODO 在组合的情况下，怎么限制一次只能买五个手机呢？
//    TODO 1）首先，不能修改MerchandiseV2这个类，否则你会限制所有商品一次购买的数量
//    TODO 2）其次，在现实情况下，这个类可能根本不受你控制，你无权修改其代码
//    TODO 3）在每次调用buy方法的地方做限制，是不行的
//    TODO      -你无法控制别人怎么用你的类
//    TODO      -而且会面临到处复制代码的糟糕情况
//    TODO      -如果说限制改到10个，所有的复制代码都要修改，程序员都应该很懒，这不是一个程序员该做的事情
//    TODO 4）在只能修改手机类的情况下，我们可以提供一个buyPhone的方法，实现限制购买数量的逻辑
//    TODO   但是这样并不能阻止别人像下面这样调用Merchandise的bug方法，这样方法是会修改库存的，所以还是无法硬性的限制一次性的赋值

// >> TODO 我们来理清一下自己的核心诉求：针对手机，限制一次性的购买量，必须限制死，必须不影响别的商品，必须只能改手机类的代码
//    TODO 这时候，组合就无能为力了，继承可以发挥其应有的作用。

// >> TODO 继承不是组合，继承也不只是为了能简单的拿来父类的属性和方法。如果仅仅如此，原封不动的拿来主义，组合也能做到。
//    TODO 继承也不是通过组合的方式来实现的。和组合相比，继承更像是融合。

public class PhoneExtendsMerchandise extends MerchandiseV2 {

    // 给Phone增加新的属性和方法
    private double screenSize;
    private double cpuHZ;
    private int memoryG;
    private int storageG;
    private String brand;
    private String os;


}
