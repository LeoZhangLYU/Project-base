package code020;

public class AssignArray {
    public static void main(String[] args) {
        int[] book = new int[3];
        book[0] = 9;
        System.out.println("book长度为" + book.length + "。book[0] = " + book[0]);


        book = new int[32];

        System.out.println("book长度为" + book.length + "。book[0] = " + book[0]);
    }
}
