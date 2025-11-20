package string;

import java.util.Scanner;

public class CountVowelsDemo {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.print("\nEnter T");
        int T = sc.nextInt();

        String s= sc.nextLine();

        String vowels = "aeiouAEIOU";
        int count=0;

    for(int  i=0;i<T;i++){
        if(s==vowels){
            count++;
        }
    }
    System.err.println(count);
    }
}
