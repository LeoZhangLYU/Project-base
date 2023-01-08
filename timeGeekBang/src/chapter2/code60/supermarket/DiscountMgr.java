package chapter2.code60.supermarket;

public class DiscountMgr {
    public static double BASE_DISCOUNT;
    public static double VIP_DISCOUNT;
    public static double SVIP_DISCOUNT;

    // >> TODO 其实给静态变量赋值也是放在代码块里面的，static代码块可以有多个，是从上而下执行的。
    //    TODO 可以认为这些代码都被组织到了一个client方法里面
    public static double WHERE_AM_I;

    static {
        BASE_DISCOUNT = 0.99;
        VIP_DISCOUNT = 0.85;
        SVIP_DISCOUNT = 0.75;

        // >> TODO 使用某个静态变量的代码块必须在静态变量后面
        // >> TODO （但是仅仅赋值没有限制）
        System.out.println("静态代码块1里的SVIP_DISCOUNT" + SVIP_DISCOUNT);

        // >> TODO 这段代码在哪个方法中呢？client 即class init。会在每个class初始化时被调用一次
        // SVIP_DISCOUNT = 9 / 0;
    }

    static {
        SVIP_DISCOUNT = 0.1;
        System.out.println("静态代码块1里的SVIP_DISCOUNT" + SVIP_DISCOUNT);
    }

    public static void main(String[] args) {
        System.out.println("最终main 方法中使用的SVIP_DISCOUNT是" + SVIP_DISCOUNT);
    }


}
