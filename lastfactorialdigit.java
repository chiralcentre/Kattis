import java.util.Scanner;

public class lastfactorialdigit {
    public static int lastFactorialDigit(int n){
        if (n == 0) {return 1;}
        else if (n == 1) {return 1;}
        else if (n == 2) {return 2;}
        else if (n == 3) {return 6;}
        else if (n == 4) {return 4;}
        else {return 0;}
    }
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt(), counter = 0;
        while (counter < n){
            int a = s.nextInt();
            System.out.println(lastFactorialDigit(a));
            counter += 1;
        }
        s.close();
    }
}
