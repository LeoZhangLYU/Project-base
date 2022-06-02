package code018;

/**
 * 生成一个在指定范围内的随机正整数程序关键点
 * 1 得到随机数，java支持得到的0到1的double类型的随机数
 * 2 确定基本的数学方法
 * 3 运用取模运算符
 * 4 使用强制类型转换
 * 5 确保生成的数字在指定的范围内。极限思维，假设随机数是0或者1，结果是多少；假设取模后是0或者mod-1，结果会是多少。
 */
public class Comments {
    public static void main(String[] args) {
        double random = 0;

//        要生成一个大于0.5的随机数，只有随机数大于了0.5，循环才会退出。
        while (random < 0.5) {

            random = Math.random();
            System.out.println(random);
        }

        System.out.println("生成的大于0.5的随机数是" + random);

        int rangeStart = 30;
        int rangeEnd = 90;

        int mod = rangeEnd - rangeStart;

        int bigRandom = (int) (Math.random() * (rangeEnd * 100));

        System.out.println("mod="+mod+",bigrandom="+bigRandom);
    }
}
