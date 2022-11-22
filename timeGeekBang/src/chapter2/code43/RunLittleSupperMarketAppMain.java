package chapter2.code43;

import chapter2.code43.supermarket.LittleSuperMarketV2;
import chapter2.code43.supermarket.MerchandiseV2;

public class RunLittleSupperMarketAppMain {

    public static void main(String[] args) {
        // 创建一个小超市
        LittleSuperMarketV2 littleSuperMarket = new LittleSuperMarketV2();
        littleSuperMarket.address = "世纪大道666号";
        littleSuperMarket.superMarketName = "有家超市";
        littleSuperMarket.parkingCount = 200;
        littleSuperMarket.merchandises = new MerchandiseV2[200];
        littleSuperMarket.merchandiseSold = new int[littleSuperMarket.merchandises.length];

        // 为了使用方便，创建一个商品数据引用，和littleSuperMarket.merchandises指向同一个数组对象
        MerchandiseV2[] all = littleSuperMarket.merchandises;
        for (int i = 0; i < all.length; i++) {
            MerchandiseV2 m = new MerchandiseV2();
            m.count = 200;
            m.id = "ID" + i;
            m.name = "商品" + i;
            m.purchasePrice = Math.random() * 200;
            m.soldPrice = (1 + Math.random()) * 200;
            all[i] = m;
        }

        System.out.println("下面请利润最高的商品自我介绍");
        // >> TODO 返回值可以直接使用，不必赋值给一个变量再使用
        littleSuperMarket.getBiggestProfitMerchindese().describe();

    }
}
