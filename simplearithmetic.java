import java.math.*;
import java.util.Scanner;

public class simplearithmetic {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        BigDecimal a = input.nextBigDecimal(), b = input.nextBigDecimal(), c = input.nextBigDecimal();
        MathContext mc = new MathContext(100, RoundingMode.HALF_UP) ;
        System.out.println(a.multiply(b.divide(c,mc),mc));
        input.close();
    }
}
