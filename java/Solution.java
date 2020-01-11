import java.util.Scanner;

public class Solution {

	public static void diamondOfStars(String args[]) {
		//Your Code goes here

	    Scanner s=new Scanner(System.in);
	    int n=s.nextInt();
        int i=1,p=(n+1)/2;
        while (i<=n){
            
            int spaces=1;
            while(spaces<=p-i+1){
                System.out.print(' ');
                spaces+=1;
                
            }
            int stars=1;
            while(stars<=i){
                System.out.print('*');
                stars+=1;
            }
            int rem_stars=stars-1;
            while(rem_stars<=p){
                System.out.print('*');
                rem_stars+=1;
            }
            
            
            
            
            i+=1;
        }
       
       
	}
//System.our.print(diamondOfStars(k));
}