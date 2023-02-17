package chapter2.code66.learn;

// >> TODO System类中有很多和系统相关的方法。我们用的最多的就是in和out来读取和输出数据
// >> TODO System中另一个最常用的，无可替代的方法：取当前的时间。
public class LearnSystem {
    public static void main(String[] args) {
        long startMS = System.currentTimeMillis();

        int counter = 0;
        for (int i = 0; i < 1000; i++) {
            counter++;
        }

        long endMS = System.currentTimeMillis();
        System.out.println("程序执行了几个毫秒？" + (endMS - startMS));

        long startNS = System.nanoTime();
        counter = 0;
        for (int i = 0; i < 1000; i++) {
            counter++;
        }

        long endNS = System.nanoTime();
        System.out.println("程序执行了几个纳秒？" + (endNS - startNS));
    }
}
