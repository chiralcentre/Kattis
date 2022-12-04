import java.io.*;

public class isiteven {
    public static int twoPower(int n) {
        int ans = 0;
        while (n % 2 == 0) {
            n >>= 1;
            ans += 1;
        }
        return ans;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]), K = Integer.parseInt(firstLine[1]);
        int exponent = 0;
        for (int i = 0; i < N; i++) exponent += twoPower(Integer.parseInt(br.readLine()));
        pw.println(exponent >= K ? "1" : "0");
        br.close();
        pw.close();
    }
}
