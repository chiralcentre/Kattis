import java.util.Scanner;

public class detaileddifferences {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
        for (int i = 0; i < n; i++){
            String s1 = s.nextLine().strip(), s2 = s.nextLine().strip(), result = "";
            // s1 and s2 have same lengths
            for (int j = 0; j < s1.length(); j++){
                result += (s1.charAt(j) == s2.charAt(j) ? "." : "*");
            }
            System.out.println(s1);
            System.out.println(s2);
            System.out.println(result);
            System.out.println(); // blank line
        }
        s.close();
    }
}
