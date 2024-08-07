import java.io.*;
import java.util.*;

public class fyrirtaekjanafn {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String s = br.readLine().strip();
        HashSet<Character> vowels = new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'y'));
        for (int i = 0; i < s.length(); i++) { if (vowels.contains(Character.toLowerCase(s.charAt(i)))) pw.print(s.charAt(i)); }
        pw.println();
        br.close();
        pw.close();
    } 
}
