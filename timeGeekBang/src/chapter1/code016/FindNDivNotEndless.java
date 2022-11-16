package chapter1.code016;

public class FindNDivNotEndless {
    public static void main(String[] args) {
        int num = 5;

        int divided = 100;
        int divisor = 2000000000;

        int found = 0;

        String start = "从" + divided + "开始，";

        while (found < num) {
            if (divided < 0) {
                System.out.println("被除数溢出，计算结束");
                break;
            }
            if (divided % divisor == 0) {
                found++;
                System.out.println(divided + "可以整除" + divisor + "，商为" + divided % divisor);
            }
            divided++;
        }

        System.out.println(start + "共找到" + found + "个可以整除" + divisor + "的数。");
        System.out.println(divided);
    }
}
