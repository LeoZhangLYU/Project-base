package chapter2.code64.learn.AI;

import java.util.Scanner;

public class AIAppMain {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        AI ai = new AI();

        while (true) {
            String input = in.next();
            if ("exit".equals(input)) {
                System.out.println("goodbye");
                break;
            }
            String answer = ai.answer(input);
            System.out.println(answer);
        }
    }
}
