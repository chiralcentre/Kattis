import java.io.*;
import java.util.*;

public class subarrays {
    public static String solve(long[] arr, int N, long B) {
        long[] prefixSums = new long[N];
        prefixSums[0] = arr[0];
        for (int i = 1; i < N; i++) prefixSums[i] = prefixSums[i - 1] + arr[i];
        // map every prefix sum to the first index which it occurs
        HashMap<Long,Integer> sumToIndices = new HashMap<>();
        int L = 1000000, R = 1000000;
        for (int i = 0; i < N; i++) {
            if (prefixSums[i] == B) {
                return String.format("0 %d",i);
            } else {
                int index = sumToIndices.getOrDefault(prefixSums[i] - B, 1000000);
                if (index + 1 < L) {
                    L = index + 1; R = i;
                }
            }
            sumToIndices.putIfAbsent(prefixSums[i], i);
        }
        return (L == 1000000 && R == 1000000) ? "-1" : String.format("%d %d",L,R);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        String[] firstLine = br.readLine().split(" "), secondLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        long K = Long.parseLong(firstLine[1]), B = Long.parseLong(firstLine[2]);
        long[] arr = new long[N];
        for (int i = 0; i < N; i++) arr[i] = Long.parseLong(secondLine[i]) - K;
        pw.println(solve(arr,N,B));
        br.close();
        pw.close();
    }
}
