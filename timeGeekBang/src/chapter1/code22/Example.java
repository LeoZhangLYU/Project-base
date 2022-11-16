package chapter1.code22;

import java.util.Scanner;

public class Example {

    public static void main(String[] args) {

        //        声明六个变量，分别代表六门科目的成绩
        int YuWenIndex = 0;
        int ShuXueIndex = 1;
        int WaiYuIndex = 2;
        int WuLiIndex = 3;
        int HuaXueIndex = 4;
        int ShengWuIndex = 5;

        int totalScoreCount = 6;

//        每门课的名字
        String[] names = new String[totalScoreCount];
        names[YuWenIndex] = "语文";
        names[ShuXueIndex] = "数学";
        names[WaiYuIndex] = "外语";
        names[WuLiIndex] = "物理";
        names[HuaXueIndex] = "化学";
        names[ShengWuIndex] = "生物";

        Scanner in = new Scanner(System.in);
        System.out.println("请问要保存几年的成绩：");
        int yearCount = in.nextInt();

        double[][] scores = new double[yearCount][totalScoreCount];

        for (int i = 0; i < yearCount; i++) {
            for (int j = 0; j < totalScoreCount; j++) {
                scores[i][j] = 80 + Math.random() * 20;
                System.out.println("第" + (i + 1) + "年" + names[j] + "成绩为：" + scores[i][j]);
            }
        }

        boolean cont = true;
        while (cont) {
            System.out.println("请输入要进行的操作编号");
            System.out.println("1.求某年最好的成绩\n" + "2.求某年的平均成绩\n" +
                "3.求所有年份最好成绩\n" + "4.求某门课历年最好成绩\n");

            int oprtId = in.nextInt();

            int year = 0;
            switch (oprtId) {
                case 1:
                    System.out.println("请输入要求哪一年的最好成绩");
                    year = in.nextInt() - 1;
                    if (year < 0 || year >= yearCount) {
                        System.out.println("年份非法");
                        break;
                    }
                    int bestOfYearScoreId = 0;
                    for (int i = 0; i < scores[year].length; i++) {
                        if (scores[year][bestOfYearScoreId] < scores[year][i]) {
                            bestOfYearScoreId = i;
                        }
                    }
                    System.out.println("第" + (year + 1) + "年最好成绩为" + names[bestOfYearScoreId] + ":"
                        + scores[year][bestOfYearScoreId]);
                    break;
                case 2:
                    System.out.println("请输入要求哪一年的平均成绩");
                    year = in.nextInt() - 1;
                    if (year < 0 || year >= yearCount) {
                        System.out.println("年份非法");
                        break;
                    }
                    double totalScore = 0;
                    for (int i = 0; i < scores[year].length; i++) {
                        totalScore += scores[year][i];
                    }
                    System.out.println("第" + (year + 1) + "年的平均成绩为" + (totalScore / names.length));
                    break;
                case 3:
                    int beatOfYearsScoreId = 0;
                    year = 0;
                    for (int i = 0; i < scores.length; i++) {
                        for (int j = 0; j < scores[i].length; j++) {
                            if (scores[year][beatOfYearsScoreId] < scores[i][j]) {
                                year = i;
                                beatOfYearsScoreId = j;
                            }
                        }
                    }
                    System.out.println(
                        "历年最好成绩为第" + (year + 1) + "年的" + names[beatOfYearsScoreId] + "成绩："
                            + scores[year][beatOfYearsScoreId]);
                    break;
                case 4:
                    System.out.println("请问要查询哪门课的历年最好成绩：");
                    int scoreId = in.nextInt();
                    for (int i = 0; i < scores.length; i++) {
                        if (scores[year][scoreId] < scores[i][scoreId]) {
                            year = i;
                        }
                    }
                    System.out.println(names[scoreId] + "历年最好成绩为第" + (year + 1) + "年，成绩为："
                        + scores[year][scoreId]);
                    break;
                default:
                    System.out.println("程序结束");
                    cont = false;
                    break;
            }
        }
    }
}
