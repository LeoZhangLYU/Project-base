package chapter2.code42;

import chapter2.code42.person.Customer;
import chapter2.code42.supermarket.LittleSuperMarket;
import chapter2.code42.supermarket.Merchandise;
import java.util.Scanner;

/**
 * @author P0192310
 */
public class RunLittleSupperMarketAppMain {

    public static void main(String[] args) {
        LittleSuperMarket littleSuperMarket = new LittleSuperMarket();
        littleSuperMarket.address = "世纪大道666号";
        littleSuperMarket.superMarketName = "有家超市";
        littleSuperMarket.parkingCount = 200;
        littleSuperMarket.merchandises = new Merchandise[200];
        littleSuperMarket.merchandiseSold = new int[littleSuperMarket.merchandises.length];

        Merchandise[] all = littleSuperMarket.merchandises;
        for (int i = 0; i < all.length; i++) {
            Merchandise m = new Merchandise();
            m.count = 200;
            m.id = "ID" + i;
            m.name = "商品" + i;
            m.purchasePrice = Math.random() * 200;
            m.soldPrice = (1 + Math.random()) * 200;
            all[i] = m;
        }

        System.out.println("超市开门了");

        boolean open = true;
        Scanner scanner = new Scanner(System.in);
        while (open) {
            System.out.println("本店叫做：" + littleSuperMarket.superMarketName);
            System.out.println("本店地址：" + littleSuperMarket.address);
            System.out.println("共有停车位" + littleSuperMarket.parkingCount + "个");
            System.out.println("今天的营业额为" + littleSuperMarket.incomingSum);
            System.out.println("共有商品" + littleSuperMarket.merchandises.length + "种");

            Customer customer = new Customer();
            customer.name = "顾客编号" + ((int) (Math.random() * 10000));
            customer.money = (1 + Math.random()) * 1000;
            customer.isDrivingCar = Math.random() > 0.5;

            if (customer.isDrivingCar) {
                if (littleSuperMarket.parkingCount > 0) {
                    littleSuperMarket.parkingCount--;
                    System.out.println(
                        "欢迎光临，" + littleSuperMarket.superMarketName + "。本店停车免费");
                } else {
                    System.out.println("欢迎您下次再来");
                }
            } else {
                System.out.println("欢迎光临，" + littleSuperMarket.superMarketName);
            }

            double totalCoat = 0;
            while (true) {
                System.out.println("本店提供" + all.length + "种商品，欢迎选购。请输入商品编号");
                int index = scanner.nextInt();

                if (index < 0) {
                    break;
                } else if (index > all.length) {
                    System.out.println(
                        "很抱歉，本店没有这种商品，请输入编号在0到" + all.length + "之间的商品编号。");
                    continue;
                }
                Merchandise m = all[index];

                System.out.println(
                    "您选购的商品名字" + m.name + "。单价是" + m.soldPrice + "。请问您要购买多少个");
                int numToBuy = scanner.nextInt();

                if (numToBuy <= 0) {
                    System.out.println("不买看看也好，欢迎继续挑选");
                    continue;
                } else if (numToBuy > m.count) {
                    System.out.println("本店商品没有足够的数量，欢迎继续挑选");
                    continue;
                }

                if (numToBuy * m.purchasePrice + totalCoat > customer.money) {
                    System.out.println("您带的钱不够，欢迎继续挑选");
                }

                totalCoat += numToBuy * m.soldPrice;

                m.count -= numToBuy;
                littleSuperMarket.merchandiseSold[index] += numToBuy;
            }

            customer.money -= totalCoat;
            if (customer.isDrivingCar) {
                littleSuperMarket.parkingCount++;
            }
            System.out.println("顾客" + customer.name + "共消费了" + totalCoat);

            littleSuperMarket.incomingSum += totalCoat;

            System.out.println("还继续营业吗？");
            open = scanner.nextBoolean();
        }

        System.out.println("超市关门了");
        System.out.println("今天总的营业额为" + littleSuperMarket.incomingSum + "。营业情况如下");

        for (int i = 0; i < littleSuperMarket.merchandiseSold.length; i++) {
            Merchandise m = all[i];
            int numSold = littleSuperMarket.merchandiseSold[i];

            if (numSold > 0) {
                double inComing = m.soldPrice * numSold;
                double netIncoming = (m.soldPrice - m.purchasePrice) * numSold;
                System.out.println(m.name + "售出了" + numSold + "个。销售额为" + inComing + "。净利润为"
                    + netIncoming);
            }
        }
    }

}
