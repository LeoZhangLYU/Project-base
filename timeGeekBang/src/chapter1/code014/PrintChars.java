package chapter1.code014;

public class PrintChars {
    public static void main(String[] args) {
        char ch;
        ch = 'A';
        int startNum = ch;
        for (int i = 0; i < 26; i++) {
            int newNum = startNum + i;
            System.out.println(newNum + "\t" + (char) newNum);
        }
    }
}
