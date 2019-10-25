public class leap_year {

    public static void main(String[] args) {
        int year = 1900;
        if (year % 4 == 0) {
            if (year % 100 == 0) {
                if (year % 400 == 0) {
                    System.out.println("leap year");
                }
                System.out.println(" not leap year");
            } else
            {
                System.out.println("leap year" + year);
            }

    }


    }
}