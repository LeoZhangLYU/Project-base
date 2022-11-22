package chapter2.code43;

import chapter2.code43.supermarket.LittleSuperMarketV2;
import chapter2.code43.supermarket.MerchandiseV2;
import java.util.Scanner;

public class RunLittleSupperMarketAppMainExample {

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

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("今日超市大特惠，所有商品第二件半价！选择要购买的商品索引：");
            int index = scanner.nextInt();

            if (index < 0) {
                System.out.println("欢迎光临，下次再来");
                break;
            }
            System.out.println("请输入要购买的数量");
            int count = scanner.nextInt();

            MerchandiseV2 m = littleSuperMarket.merchandises[index];
            double totalCost = m.bugAndPrintLeft(count, true);
            System.out.println("商品总价为" + totalCost);
        }

    }
}
