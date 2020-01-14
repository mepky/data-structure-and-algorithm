package Function;

public class NcR {
    public static void main (String[] args) {
        int n=10,r=6;
        int factn=1,factr=1,factnr=1;
        for(int i=2;i<=n;i++)
        {
            factn*=i;
            if(i<=r)
                factr*=i;
            if(i<=n-r)
                factnr*=i;
        }
        int ncr=factn/(factr*factnr);
        System.out.print(ncr);
    }
}
