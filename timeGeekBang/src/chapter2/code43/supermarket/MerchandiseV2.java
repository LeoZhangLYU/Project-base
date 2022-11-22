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
    // >> TODO 方法体内部定义的变量叫做局部变量
    public void describe() {
        System.out.println(
            "商品名字叫做" + name + "，id是" + id + "。 商品售价是" + soldPrice + "。商品进价是"
                + purchasePrice + "。商品库存量是" + count + "。销售一个的毛利润是" + (soldPrice
                - purchasePrice) + "。生产地址为：" + madeIn);
    }

    /**
     * 在方法定义中指定方法的返回值类型 java中一个方法只能有一种返回值，如果不需要返回值则用void表示 如果定义了返回值，则必须使用 return 语句返回方法的返回值。return 是
     * java 的关键字 可以认为，返回值必须要能够用来给返回值类型的变量赋值
     */
    public double calculateProfit() {
        double profit = soldPrice - purchasePrice;
        // >> TODO 这个return是代码块里面的return，是return所在代码块的最后一个语句
        if (profit <= 0) {
            return 0;
        }
        // >> TODO return语句必须是所在代码块的最后一个语句，否则就是语法错误
        return profit;

        // >> TODO 一个方法可以有多个返回语句
    }

    // >> TODO 返回值如果是基本类型，则要类型完全相同，或者符合类型自动转换原则
    public double getCurrentCount() {
        return count;
    }

    // >> TODO 如果不符合规则，可以使用强制类型转换
    public int getIntSoldPrice() {
        return (int) soldPrice;
    }

    // >> TODO 参数是定义在方法名称后面的括号里的
    // >> TODO 参数定义的规范和变量一样，都是类型名字加标识符，这里的标识符我们叫做参数名
    // >> TODO 方法体中的代码可以使用参数
    // >> TODO 参数的值在调用方法的时候需要给出，有的资料叫做实参（实际参数）
    //    TODO 对应的，方法定义这里的参数，叫做形参（形式参数）

    /**
     * 第二件半价函数
     */
    public double buyHalf(int countToBuy) {
        if (count < countToBuy) {
            System.out.println("商品库存不足");
            return -1;
        }

        System.out.println("商品单价为" + purchasePrice);
        int fullPriceCount = countToBuy / 2 + countToBuy % 2;
        int halfPriceCount = countToBuy - fullPriceCount;

        double totalCost = fullPriceCount * purchasePrice + halfPriceCount * purchasePrice / 2;
        count -= countToBuy;
        return totalCost;
    }

    // >> TODO 一个方法可以有多个参数，多个参数之间用逗号隔开
    public double bugAndPrintLeft(int countToBuy, boolean printLeft) {
        if (count < countToBuy) {
            System.out.println("商品库存不够");
            if (printLeft) {
                System.out.println("商品剩余库存为" + count);
            }
            return -1;
        }

        System.out.println("商品单价为" + purchasePrice);
        int fullPriceCount = countToBuy / 2 + countToBuy % 2;
        int halfPriceCount = countToBuy - fullPriceCount;

        double totalCost = fullPriceCount * purchasePrice + halfPriceCount * purchasePrice / 2;
        count -= countToBuy;

        if (printLeft) {
            System.out.println("商品剩余库存为" + count);
        }

        return totalCost;
    }

    // >> TODO 参数可以是任何类型，包括自定义类型，甚至是自己的类型都没问题
    public boolean totalValueBiggerThan(MerchandiseV2 merchandiseV2) {
        return count * purchasePrice > merchandiseV2.purchasePrice * merchandiseV2.count;
    }
}
