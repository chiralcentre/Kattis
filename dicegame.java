import java.util.Scanner;

public class dicegame {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a1 = s.nextInt(), b1 = s.nextInt(), a2 = s.nextInt(), b2 = s.nextInt(), a3 = s.nextInt(), b3 = s.nextInt(), a4 = s.nextInt(), b4 = s.nextInt();
        System.out.println(a1 + b1 + a2 + b2 > a3 + b3 + a4 + b4 ? "Gunnar" : (a1 + b1 + a2 + b2 < a3 + b3 + a4 + b4 ? "Emma" : "Tie"));
        s.close();
    }
}
