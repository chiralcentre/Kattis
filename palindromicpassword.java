import java.util.*;
import java.io.*;

public class palindromicpassword {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        //get all palindromic six digit numbers
        TreeSet<Integer> ts = new TreeSet<>();
        for (Integer i = 100; i <= 999; i++) {
            String s = i.toString();
            for (int j = 2; j >= 0; j--) s += s.charAt(j);
            ts.add(Integer.parseInt(s));
        }
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int u = Integer.parseInt(br.readLine());
            Integer b = ts.floor(u), t = ts.ceiling(u);
            if (b == null) pw.println(t);
            else pw.println(u - b <= t - u ? b : t);
        }
        br.close();
        pw.close();
    }
}
