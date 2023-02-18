package chapter2.code67;

public class LearnStringBuilder {

    public static void main(String[] args) {
        // >> TODO StringBuilder首先是可变的
        //    TODO 而且对它进行操作的方法，都会返回this自引用。这样我们就可以一直点下去，对String进行构造。
        StringBuilder stringBuilder = new StringBuilder("");

        long longVal = 123456789;

        stringBuilder.append(true).append("abc").append(longVal);

        System.out.println(stringBuilder.toString());
        System.out.println(stringBuilder.reverse().toString());
        System.out.println(stringBuilder.reverse().toString());
        System.out.println(stringBuilder.toString());

        System.out.println(stringBuilder.delete(0, 4).toString());
        System.out.println(stringBuilder.insert(3, "LLL").toString());
    }
}
