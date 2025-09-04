import java.util.Scanner;

public class Reverse_natural_Number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = sc.nextInt();

        for (int i = n; i >=1; i--) {
            System.out.println(i);
            
        }
    }
}
