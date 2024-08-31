import java.io.*;
import java.util.*;

public class subaruba {
    public static final HashSet<Character> VOWELS = new HashSet<Character>(Arrays.asList('A', 'E', 'I', 'O', 'U', 'Y'));

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String firstLine = br.readLine().strip();
        int n = Integer.parseInt(br.readLine());
        if (firstLine.equals("A")) {
            for (int i = 0; i < n; i++) {
                String line = br.readLine().strip();
                int j = 0;
                while (j < line.length()) {
                    boolean upper = false, found = false;
                    if (Character.toLowerCase(line.charAt(j)) == 'u' && j + 1 < line.length() && line.charAt(j + 1) == 'b') {
                        upper = Character.isUpperCase(line.charAt(j));
                        found = true;
                        j += 2;
                    }
                    pw.print((found && upper) ? Character.toUpperCase(line.charAt(j)) : line.charAt(j));
                    j++;
                }
                pw.print("\n");
            }
        } else {
            for (int i = 0; i < n; i++) {
                String line = br.readLine().strip();
                int j = 0;
                while (j < line.length()) {
                    if (VOWELS.contains(Character.toUpperCase(line.charAt(j)))) pw.print(Character.isUpperCase(line.charAt(j)) ? "Ub" : "ub");
                    pw.print(line.charAt(j));
                    j++;
                }
                pw.print("\n");
            }
        }
        br.close();
        pw.close();
    }
}