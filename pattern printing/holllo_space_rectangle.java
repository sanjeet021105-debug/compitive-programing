import java.util.Scanner;

public class holllo_space_rectangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter n: ");
        int n = sc.nextInt();

        for (int i = 1; i <=n; i++) {
            for (int j = 1; j <=n; j++) {
                if (j==1 || j==5) {
                    System.out.print("*");
                    
                }else
                {
                    System.out.print("_");
                }
                
            }System.out.println();
            
        }
    }
}
