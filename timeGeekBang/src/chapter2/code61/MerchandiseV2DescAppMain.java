package chapter2.code61;

import chapter2.code61.supermarket.MerchandiseV2;

public class MerchandiseV2DescAppMain {

    public static void main(String[] args) {
        // >> TODO 非共有的类，不能在包外被使用
        // NonPublicClassCanUseAnyName nonPublicClassCanUseAnyName;
        MerchandiseV2 merchandiseV2 = new MerchandiseV2("书桌", "DESK9527", 40, 999.9, 500);
        merchandiseV2.describe();
    }

}
