import java.io.*;

public class sumkindofproblem {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int P = Integer.parseInt(br.readLine());
        for (int i = 1; i <= P; i++){
            String[] line = br.readLine().split(" ");
            int N = Integer.parseInt(line[1]);
            // sum of AP
            long s1 = (N*(N+1))/2, s2 = N*N, s3 = N*(N+1);
            pw.printf("%d %d %d %d %n",i,s1,s2,s3);
        }
        br.close();
        pw.close();
    }
}
