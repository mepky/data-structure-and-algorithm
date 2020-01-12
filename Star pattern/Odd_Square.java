import java.util.Scanner;

public class Odd_Square {

    public static void main(String[] args) {
        // Write your code here

        Scanner s=new Scanner(System.in);

        int n=s.nextInt();

        int i=1;
        while(i<=n){
            int j=1,p=i;
            while(j<=n-i+1){
                    System.out.print(2*p - 1);
                    j += 1;
                    p+=1;
                }

            int k=1;
            while(k<=i-1) {
            System.out.print(2*k-1);
            k+=1;
            }

            System.out.println();

            i+=1;
        }








    }
}
