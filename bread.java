import java.io.*;
import java.util.*;

public class bread {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine());
        String[] firstLine = br.readLine().split(" "), secondLine = br.readLine().split(" ");
        int[] p1 = new int[N], p2 = new int[N], second = new int[N];
        for (int i = 0; i < N; i++) {
            p1[i] = Integer.parseInt(firstLine[i]);
            p2[i] = Integer.parseInt(secondLine[i]);
        }

        for (int i = 0; i < N; i++) second[p1[i] - 1] = p2[i];
        boolean[] seen = new boolean[N];
        int swaps = N;
        //O(N)
        for (int i = 0; i < N; i++) {
            if (!seen[i]) {
                swaps--;
                int j = i;
                while (!seen[j]) {
                    seen[j] = true;
                    j = second[j] - 1;
                }
            }
        }
        pw.print(swaps%2 == 1 ? "Impossible\n" : "Possible\n");
        br.close();
        pw.close();
    }
}
