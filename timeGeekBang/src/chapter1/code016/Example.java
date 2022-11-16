package chapter1.code016;

public class Example {
    public static void main(String[] args) {
        int num = 10;

        int divided = 100;
        int divisor = 89;

        int found = 0;

        while (found < num) {
            if (divided % divisor == 0) {
                found++;
                System.out.println(divided + "可以整除" + divisor + "，商为" + divided % divisor);
            }
            divided++;
        }
    }
}
