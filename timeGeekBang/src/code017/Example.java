package code017;

public class Example {
    public static void main(String[] args) {
        int n = 5;
        String string = n+"对应的中文数字是：";

        switch (n){
            case 1:
                string += "壹";
                break;
            case 2:
                string += "贰";
                break;
            case 3:
                string += "叁";
                break;
            case 4:
                string += "肆";
                break;
            case 5:
                string += "伍";
                break;
            case 6:
                string += "陆";
                break;
            case 7:
                string += "柒";
                break;
            case 8:
                string += "捌";
                break;
            case 9:
                string += "玖";
                break;
            default:
                System.out.println("错误的值，"+n+"。值需要大于等于1，小于等于9");
        }
        System.out.println(string);
    }
}
