import java.util.Scanner;

public class aaah {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String s1 = s.nextLine().strip(), s2 = s.nextLine().strip();
        System.out.println(s1.length() >= s2.length() ? "go": "no");
        s.close();
    }
}
