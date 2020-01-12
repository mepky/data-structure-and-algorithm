import java.util.Scanner;
public class Solution {
//THis of for low integer till 5
    public static void main(String[] args) {
        // Write your code here
        Scanner s=new Scanner(System.in);
        int p=s.nextInt();
        int n=2*p+1,m=1;


        System.out.println('*');
        int k=1,t=1;
        while(k<=p){
            System.out.print("*"+t*t+"*");
            System.out.println();
            t=t*10+1;
            k+=1;

        }
        int i =1;
        t=t/100;
        while (i<p){
            System.out.print("*"+t*t+"*");
            System.out.println();
            t=t/10;
            i+=1;
        }
        System.out.println('*');


    }
}