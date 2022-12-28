package chapter2.code52.supermarket;

public class LittleSuperMarket {
    public String superMarketName;
    public String address;
    public int parkingCount;
    public double incomingSum;
    public MerchandiseV2[] merchandises;
    public int[] merchandisSold;

    /**
     * @param superMarketName
     * @param address
     * @param parkingCount
     * @param merchandiseCount 商品种类数
     * @param count            每种商品缺省库存
     */
    public void init(String superMarketName, String address, int parkingCount, int merchandiseCount, int count) {
        this.superMarketName = superMarketName;
        this.address = address;
        this.parkingCount = parkingCount;

        merchandises = new MerchandiseV2[merchandiseCount];
        for (int i = 0; i < merchandises.length; i++) {
            // 创建并给商品的属性赋值
            MerchandiseV2 m = new MerchandiseV2();
            m.name = "商品" + i;
            m.count = count;
            m.purchasePrice = Math.random() * 200;
            m.soldPrice = m.purchasePrice * (1 + Math.random());
            m.id = "ID" + i;
            // 用创建的商品，给商品数组的第i个引用赋值，all和小超市的商品数组引用指向的是同一个数组对象
            merchandises[i] = m;
        }
        merchandisSold = new int[merchandises.length];
    }

    public String getSuperMarketName() {
        return superMarketName;
    }

    public void setSuperMarketName(String superMarketName) {
        this.superMarketName = superMarketName;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getParkingCount() {
        return parkingCount;
    }

    public void setParkingCount(int parkingCount) {
        this.parkingCount = parkingCount;
    }

    public double getIncomingSum() {
        return incomingSum;
    }

    public void setIncomingSum(double incomingSum) {
        this.incomingSum = incomingSum;
    }

    public MerchandiseV2[] getMerchandises() {
        return merchandises;
    }

    public void setMerchandises(MerchandiseV2[] merchandises) {
        this.merchandises = merchandises;
    }

    public int[] getMerchandisSold() {
        return merchandisSold;
    }

    public void setMerchandisSold(int[] merchandisSold) {
        this.merchandisSold = merchandisSold;
    }

    // 一些特殊的逻辑

    public MerchandiseV2 getBiggestProfitMerchandise() {
        MerchandiseV2 curr = null;
        for (int i = 0; i < merchandises.length; i++) {
            MerchandiseV2 m = merchandises[i];
            // 这个逻辑有问题吗？相同的利润怎么判断？
            if (curr == null || curr.calculateProfit() < curr.calculateProfit()) {
                curr = m;
            }
        }
        return curr;
    }
}
