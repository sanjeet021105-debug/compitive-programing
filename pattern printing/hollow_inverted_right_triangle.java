public class hollow_inverted_right_triangle {
    public static void main(String[] args) {
        int n = 5;  

        for (int i = n; i >= 1; i--) {      
            System.out.print("* ");         

            for (int j = 1; j <= i - 1; j++) {  
                System.out.print("_ ");
            }

            System.out.println(" *");        
        }
    }
}
