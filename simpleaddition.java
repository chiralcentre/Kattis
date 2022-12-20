import java.util.Scanner;
import java.math.BigInteger;

public class simpleaddition {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger a = sc.nextBigInteger(), b = sc.nextBigInteger();
        System.out.println(a.add(b));
        sc.close();
    }
}
