package chapter2.code43.supermarket;

public class MerchandiseV2DescAppMain {

    public static void main(String[] args) {
        MerchandiseV2 merchandiseV2 = new MerchandiseV2();
        merchandiseV2.name = "书桌";
        merchandiseV2.soldPrice = 999.9;
        merchandiseV2.purchasePrice = 500;
        merchandiseV2.count = 400;
        merchandiseV2.id = "DESK626";
        merchandiseV2.madeIn = "CHINA";

        merchandiseV2.describe();
    }
}
