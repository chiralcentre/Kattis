import java.io.*;

public class fleytitala {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        double d = Double.parseDouble(br.readLine());
        long k = Long.parseLong(br.readLine());
        double ans = d;
        // after 17 iterations, desired accuracy is attained
        for (long i = 0; i < Math.min(17, k); i++) {
            d *= 0.5;
            ans += d;
        }
        pw.println(ans);
        br.close();
        pw.close();
    }
}
