import java.io.*;
import java.util.*;


public class bst {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine()); long counter = 0;
        TreeMap<Integer,Integer> levels = new TreeMap<>(); //key keeps track of lower bound of range, value keeps track of level
        levels.put(1,0); //start from level 0
        for (int i = 0; i < N; i++){ //O(log N) per iteration
            int a = Integer.parseInt(br.readLine());
            Map.Entry<Integer, Integer> entry = levels.floorEntry(a);
            counter += entry.getValue();
            int b = entry.getKey();
            levels.put(a, entry.getValue());
            levels.put(b,entry.getValue()+1);
            levels.put(a+1,entry.getValue()+1);
            pw.println(counter);
        }
        br.close();
        pw.close();
    }
}
