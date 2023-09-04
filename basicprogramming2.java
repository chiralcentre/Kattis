import java.io.*;
import java.util.*;

class basicprogramming2 {
    public static void solve(ArrayList<Integer> A, int N, int t, PrintWriter pw) {
        if (t == 1) {
            for (int x: A) {
                if (Collections.binarySearch(A, 7777 - x) >= 0) {
                    pw.println("YES\n");
                    return;
                }
            }
            pw.println("NO\n");
        } else if (t == 2) {
            for (int i = 1; i < N; i++) {
                if (A.get(i - 1) == A.get(i)) {
                    pw.println("Contains duplicate");
                    return;
                }
            }
            pw.println("Unique");
        } else if (t == 3) {
            for (int i = 0; i < N; i++) {
                int counter = 1;
                while (i + 1 < N && A.get(i + 1) == A.get(i)) {
                    i++;
                    counter++;
                }
                if ((counter << 1) > N) {
                    pw.println(A.get(i));
                    return;
                }
            }
            pw.println(-1);
        } else if (t == 4) {
            if (N % 2 == 1) pw.println(A.get(N >> 1));
            else pw.println(A.get((N >> 1) - 1) + " " + A.get(N >> 1));
        } else {
            Boolean first = true;
            for (int v: A) {
                if (100 <= v && v <= 999) {
                    if (!first) pw.print(" ");
                    first = false;
                    pw.print(v);
                }
            }
            pw.println();
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        String[] tokens = br.readLine().split(" ");
        int N = Integer.parseInt(tokens[0]), t = Integer.parseInt(tokens[1]);
        ArrayList<Integer> A = new ArrayList<>();
        tokens = br.readLine().split(" ");
        for (String elem: tokens) A.add(Integer.parseInt(elem));
        Collections.sort(A);
        solve(A,N,t,pw);
        br.close();
        pw.close();
    }
}