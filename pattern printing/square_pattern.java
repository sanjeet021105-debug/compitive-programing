import java.util.Scanner;

public class square_pattern{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("enter n: ");
        int n = sc.nextInt();
        System.out.print("enter m: ");
        int m = sc.nextInt();

        for (int i = 1; i <=n; i++) {
            for (int j = 1; j <=m; j++) {
                System.out.print("*");
            }System.out.println();
            
        }
        
    }
}