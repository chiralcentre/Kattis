import java.util.Scanner;

public class triarea {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int h = s.nextInt(), b = s.nextInt();
        System.out.println((float)h*b/2);
        s.close();
    }
}
