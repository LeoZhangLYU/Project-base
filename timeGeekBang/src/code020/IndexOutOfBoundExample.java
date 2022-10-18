package code020;

public class IndexOutOfBoundExample {
    public static void main(String[] args) {

//        数组过界
        int[] array = new int[5];
        System.out.println(array[array.length]);

//        数组不过界
        System.out.println(array[array.length - 1]);


    }
}
