package java;

import java.util.Scanner;

public class View {
    Scanner in = new Scanner(System.in);

    public int getValue(String Title) {
        System.out.printf("%s", Title);
        return in.nextInt();
    }

    public void print(int data, String title) {
        System.out.printf("%s %d", title, data);
    }
}