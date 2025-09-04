import java.util.Scanner;

public class sum_of_Natural_number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = sc.nextInt();
        int sum=0;

        for (int i = 1; i <=n; i++) {
            sum+=i;    
        } System.out.print(sum);
    }
    
}
