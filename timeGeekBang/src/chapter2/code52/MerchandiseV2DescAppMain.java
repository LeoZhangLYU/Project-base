package chapter2.code52;

import chapter2.code52.supermarket.MerchandiseV2;

public class MerchandiseV2DescAppMain {
    public static void main(String[] args) {
        MerchandiseV2 merchandiseV2 = new MerchandiseV2();

        // >> TODO 调用方法，完成对成员变量的操作。
        merchandiseV2.init("书桌", "DESK9527", 40, 999.9, 500);
        merchandiseV2.describe();
    }
}
