
import java.util.Scanner;
public class helloWorld {


	public static void main(String[] args) {
		
		/* Your class should be named Solution.
	 	* Read input as specified in the question.
	 	* Print output as specified in the question.
		*/

        Scanner s=new Scanner(System.in);
        int basic=s.nextInt();
        char grade=s.next().charAt(0);
        double hra,da,allow,pf;
        int totalsalary;
        hra=0.2*basic;
        da=0.5*basic;
        pf=0.11*basic;
        if (grade=='A'){
            allow=1700;
        }
        else if (grade=='B'){
            
            allow=1500;
        }
        else{
            allow=1300;
        }
        totalsalary=(int)(basic+hra+da+allow-pf);
        System.out.print(totalsalary);
        	
	}

}
