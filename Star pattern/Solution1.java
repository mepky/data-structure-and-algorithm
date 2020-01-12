import java.util.Scanner;
public class Solution1 {

    public static void main(String[] args) {
        // Write your code here

        Scanner s=new Scanner(System.in);

        int n=s.nextInt();

        int i=1;
        while(i<=n){
            int spaces=1;
            while(spaces<=i-1){
                System.out.print(' ');
                spaces+=1;

            }
            int j=1;
            while(j<=n){
                System.out.print('*');
                j+=1;
            }
            i+=1;
            System.out.println();
        }

    }
}
