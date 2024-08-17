import java.util.*;
import java.io.*;

public class gangur {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String s = br.readLine().strip();
        long ans = 0, leftBraces = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '<') leftBraces++;
            else if (s.charAt(i) == '>') ans += leftBraces;
        }
        pw.println(ans);
        br.close();
        pw.close();
    }
}