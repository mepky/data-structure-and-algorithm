public class Account {

    private String number;
    private double balance;
    private String Emailaddress;
    private String phonenumber;
    private String Customername;

public Account(String number, double balance,String emailaddress,String phonenumber,String Customername)
{
    this.number=number;
    this.balance=balance;
    this.Emailaddress=emailaddress;
    this.phonenumber=phonenumber;
    this.Customername=Customername;

}
public Account()
{
    this("12354",55.25,"praveenkumar@gmail.com","7004546850","praveen kumar");
}
public void deposit(double amount)
{
    this.balance+=amount;
    System.out.println("Total amount became after depost" + amount + "is" +this.balance);
}
public void withdrawal(double amount)
{
    if (this.balance-amount<0)
    {
        System.out.println(amount + "cannot be withdrawal due to low balance");
    }
    else
    {
        this.balance-=amount;
        System.out.println("Total amount remained in account after withdrawl "+ amount+" is "+this.balance);
    }
}
public  void getname()
{
    System.out.println(this.Customername);
}
public void getbalance()
{
    System.out.println("Toatal current balance " +this.balance );
}
public void getEmailaddress()
{
    System.out.println(this.Emailaddress);
}
}