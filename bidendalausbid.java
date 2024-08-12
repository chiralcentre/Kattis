import java.io.*;

public class bidendalausbid {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(":");
        String[] secondLine = br.readLine().split(":");
        int a = Integer.parseInt(firstLine[0]), b = Integer.parseInt(firstLine[1]), c = Integer.parseInt(secondLine[0]), d = Integer.parseInt(secondLine[1]);
        int start = a * 60 + b, end = c * 60 + d;
        int ans = end - start;
        if (ans < 0) ans += 1440;
        pw.println(ans);
        br.close();
        pw.close();
    }
}