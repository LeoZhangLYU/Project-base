package chapter2.code66.learn;

public class LearnMain {
    // main方法也只是一个静态的，有String[] 做参数的，没有返回值的方法而已。它的特殊性在于java可以把main方法作为程序入口
    public static void main(String[] args) {
        System.out.println(args.length);
        for (String item : args
        ) {
            System.out.println(item);
        }
    }
}
