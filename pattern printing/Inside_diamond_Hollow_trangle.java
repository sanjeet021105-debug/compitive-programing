public class Inside_diamond_Hollow_trangle {
    public static void main(String[] args) {

        int n = 5;

        for (int i = 1; i <= 2 * n; i++) {
            System.out.print("*");
        }
        System.out.println();

        
        for (int i = 1; i < n; i++) {

            for (int j = 1; j <= n - i; j++) {
                System.out.print("*");
            }
            
            for (int k = 1; k <= 2 * i; k++) {
                System.out.print(" ");
            }

            for (int l = 1; l <= n - i; l++) {
                System.out.print("*");
            }
            System.out.println();
        }

        
        for (int i = n - 1; i >= 1; i--) {
            
            for (int j = 1; j <= n - i; j++) {
                System.out.print("*");
            }
            
            for (int k = 1; k <= 2 * i; k++) {
                System.out.print(" ");
            }

            for (int l = 1; l <= n - i; l++) {
                System.out.print("*");
            }
            System.out.println();
        }

        for (int i = 1; i <= 2 * n; i++) {
            System.out.print("*");
        }
    }
}

    