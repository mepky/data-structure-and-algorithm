import java.util.Scanner;
public class Sum_Pattern {

    public static void main(String[] args) {
        // Write your code here

        Scanner s=new Scanner(System.in);
        int n =s.nextInt();

        int i=1;
        while(i<=n){
            int j=1,plus=1;
            while(j<=i){
                System.out.print(j);
                if (plus<=i-1){
                    System.out.print('+');
                    plus+=1;
                }

                j+=1;
            }
//            int plus=1;
//            while(plus<=i-1){
//                System.out.print('+');
//            }
            System.out.print("="+((i+1)*i)/2);
            System.out.println();
            i+=1;
        }


    }
}
