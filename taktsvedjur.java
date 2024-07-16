import java.io.*;

public class taktsvedjur {
    public static void main(String[] args) throws IOException {
        PrintWriter pw = new PrintWriter(System.out);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long ans = 0, multiplier = 1, consec = 0;
        for (int i = 0; i < n; i++) {
            long x = Long.parseLong(br.readLine());
            if (x != 0) {
                consec++;
                if (consec == (multiplier << 1)) {
                    multiplier <<= 1;
                    multiplier = Math.min(8, multiplier);
                    consec = 0;
                }
                ans += x * multiplier;
            } else {
                consec = 0;
                multiplier >>= 1;
                multiplier = Math.max(1, multiplier);
            }
        }
        pw.println(ans);
        br.close();
        pw.close();
    }
}