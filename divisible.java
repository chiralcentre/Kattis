import java.io.*;
import java.util.*;

//compute prefix sums modulo d
//since max d is 1000000
//if two prefix sums have the same remainder, their difference is divisible by d
//algorithm runs in O(n + d) time
public class divisible {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int c = Integer.parseInt(br.readLine());
        for (int i = 0; i < c; i++){
            String[] testcase = br.readLine().split(" ");
            int d = Integer.parseInt(testcase[0]), n = Integer.parseInt(testcase[1]);
            int[] sequence = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int[] prefixSums = new int[n]; int counter = 0;
            //O(n)
            for (int j = 0; j < n; j++){
                counter += sequence[j];
                counter %= d;
                prefixSums[j] = counter;
            }
            //O(n)
            HashMap<Integer,Integer> remainders = new HashMap<>();
            for (int r: prefixSums){
                //put value of 1 in the hash table if key is not present else increment value by 1
                //this code has higher efficiency than checking if hashmap contains the key
                remainders.merge(r, 1, (a,b) -> a + b);
            }
            //O(d)
            long subseq = 0;
            subseq += remainders.getOrDefault(0, 0);
            for (Map.Entry<Integer, Integer> entry: remainders.entrySet()){
                int value = entry.getValue();
                subseq += (value*(value-1))/2;
            }
            pw.println(subseq);
        }
        br.close();
        pw.close();
    }
}
