import java.util.Scanner;

public class number_star_traingle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = sc.nextInt(); 
        int num = 1;

        for (int i = 1; i <= n; i++) {
            num = 1;  
            for (int j = 1; j <= i; j++) {
                if (j % 2 == 0) {
                    System.out.print("* ");
                } else {
                    System.out.print(num + " ");
                    num += 2; 
                }
            }System.out.println();

        }
    }
}