package chapter2.code64.learn;

public class LearnString2 {
    public static void main(String[] args) {
        String content = "Orange_Apple_Banana";

        char[] chars = content.toCharArray();
        for (char item : chars) {
            System.out.println(item);
        }

        String sp = "_";
        String[] s = content.split(sp);
        for (String item : s
        ) {
            System.out.println(item);
        }

        int indexOf = content.indexOf("_");
        System.out.println(indexOf);
        System.out.println(content.substring(indexOf + 1, content.length()));

        int lastIndexOf = content.lastIndexOf("_");
        System.out.println(lastIndexOf);
        System.out.println(content.substring(0, lastIndexOf));

        System.out.println(content.contains("apple"));
        System.out.println(content.contains("Apple"));
        System.out.println(content.startsWith("Orange"));
        System.out.println(content.endsWith("Banana"));

        String content2 = "Orange_Apple_Banana";
        String content3 = "orange_Apple_banana";

        //    TODO 两个String对象是否相等，一定要用equals方法
        System.out.println(content.equals(content2));
        System.out.println(content.equals(content3));
        System.out.println(content2.equals(content3));
    }
}
