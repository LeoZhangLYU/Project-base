package chapter2.code43.supermarket;

public class LittleSuperMarketV2 {

    /**
     * 超市名称
     */
    public String superMarketName;

    /**
     * 地址
     */
    public String address;

    /**
     * 停车位数量
     */
    public int parkingCount;

    /**
     * 收入总和
     */
    public double incomingSum;

    /**
     * 商品列表
     */
    public MerchandiseV2[] merchandises;
    /**
     * 对应商品销售量
     */
    public int[] merchandiseSold;

    // >> 返回值类型可以是类名，这时候实际返回的值就是这个类型的引用
    public MerchandiseV2 getBiggestProfitMerchindese() {
        MerchandiseV2 curr = null;
        for (int i = 0; i < merchandises.length; i++) {
            MerchandiseV2 m = merchandises[i];
            if (curr == null) {
                curr = m;
            } else {
                if (curr.calculateProfit() < m.calculateProfit()) {
                    curr = m;
                }
            }
        }
        return curr;
    }


}
