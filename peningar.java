import java.io.*;

public class peningar {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]); long d = Long.parseLong(firstLine[1]);
        String[] secondLine = br.readLine().split(" ");
        long[] cells = new long[n];
        for (int i = 0; i < n; i++) cells[i] = Integer.parseInt(secondLine[i]);
        long curr = 0; long ans = 0;
        while (cells[(int) curr] != 0) {
            ans += cells[(int) curr];
            cells[(int) curr] = 0;
            curr = (curr + d) % n;
        }
        pw.println(ans);
        br.close();
        pw.close();
    }
}
