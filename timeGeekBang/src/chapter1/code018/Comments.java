package chapter1.code018;

import java.util.Scanner;

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
//        创建Scanner来读取用户的键盘输入
        Scanner in = new Scanner(System.in);

//        游戏设置
        int rangeStart = 30;
        int rangeEnd = 50;
        int guessTotal = 5;

//        游戏统计
        int totalGameCount = 0;
        int correctGuessCount = 0;

//        是否结束游戏
        boolean gameEnd = false;

        while (!gameEnd) {
//            生成指定范围内的随机数
            int mod = rangeEnd - rangeStart;

            if (rangeStart < 0 || rangeEnd < 0) {
                System.out.println("开始和结束必须是正数或者是零");
            }

            if (mod <= 1) {
                System.out.println("非法的数字范围：(" + rangeStart + "，" + rangeEnd + ")");
            }

//            random*100为随机生成[0,100)以内的数字
            int bigRandom = (int) (Math.random() * (rangeEnd * 100));

            int numberToGuess = (bigRandom % mod) + rangeStart;

            if (numberToGuess <= rangeStart) {
                numberToGuess = rangeStart + 1;
            } else if (numberToGuess >= rangeEnd) {
                numberToGuess = rangeEnd - 1;
            }
//            剩余的猜测次数
            int leftToGuess = guessTotal;

            boolean currentGameCounted = false;
            boolean correctGuess = false;

            System.out.println("请输入猜测的数字，范围在(" + rangeStart + "，" + rangeEnd + ")。输入-1代表结束游戏。");
            while (leftToGuess > 0) {
                System.out.print("剩余猜测次数" + leftToGuess + "。请输入本次猜测的数字：");
                leftToGuess--;
                int guess = in.nextInt();
                if (guess <0){
                    gameEnd = true;
                    System.out.println("用户选择结束游戏");
                    break;
                }
                if (!currentGameCounted){
                    totalGameCount++;
                    currentGameCounted = true;
                }
                if (guess > numberToGuess) {
                    System.out.println("输入的数字比目标数字大");
                } else if (guess < numberToGuess) {
                    System.out.println("输入的数字比目标数字小");
                } else {
                    correctGuessCount++;
                    correctGuess = true;
                    System.out.println("输入正确");
                    break;
                }
            }
            if (!correctGuess){
                System.out.println("本次的目标数字是"+numberToGuess);
            }
            System.out.println("共进行了" + totalGameCount + "次游戏，其中猜中的次数为" + correctGuessCount);
        }

    }
}
