package Function;


import java.util.Scanner;
public class Solution5 {

    public static void main(String [] args){
        /* Your class should be named Solution
         * Don't write main().
         * Don't read input, it is passed as function argument.
         * Return output and don't print it.
         * Taking input and printing output is handled automatically.
         */

        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int [] arr=new int[n];

        for(int i=0;i<n;i++){

            arr[i]=s.nextInt();
        }
        int sum=0;
        for(int j=0;j<n;j++){
            sum+=arr[j];
        }




        System.out.print(sum);

    }

}