import java.util.Scanner;

public class laptopsticker {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int hc = s.nextInt(), wc = s.nextInt(), hs = s.nextInt(), ws = s.nextInt();
        System.out.println(wc > ws + 1 && hc > hs + 1 ? 1 : 0);
    }
}
