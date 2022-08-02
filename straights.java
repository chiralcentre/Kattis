import java.util.*;
import java.io.*;

public class straights {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        br.readLine(); //value of N not required
        int[] sequence = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(sequence); // O(N log N)
        HashMap<Integer,Integer> frequencyTable = new HashMap<>();
        for (int c: sequence){
            frequencyTable.merge(c, 1, (a,b) -> a + b);
            if (frequencyTable.containsKey(c-1)){
                frequencyTable.put(c-1,Math.max(0,frequencyTable.get(c-1)-1)); //only subtract 1 if frequency[c-1] > 0
            }
        }
        int minimum = 0;
        for (int value: frequencyTable.values()) minimum += value;
        pw.println(minimum);
        br.close();
        pw.close();
    }
}