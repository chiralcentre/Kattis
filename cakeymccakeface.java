import java.util.*;
import java.io.*;

public class cakeymccakeface {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine()), M = Integer.parseInt(br.readLine());
        int[] entries = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray(); 
        int[] exits = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray(); 
        HashMap<Integer,Integer> timeDifference = new HashMap<>();
        //O(N*M)
        for (int a: entries){
            for (int b: exits){
                if (b - a >= 0){
                    if (timeDifference.containsKey(b-a)) timeDifference.put(b - a, timeDifference.get(b-a) + 1);
                    else timeDifference.put(b - a, 1);
                }
            }
        }
        int answer = 0, highestFrequency = 0;
        for (Map.Entry<Integer,Integer> entry: timeDifference.entrySet()){
            if (entry.getValue() > highestFrequency){
                answer = entry.getKey();
                highestFrequency = entry.getValue();
            }
            if (entry.getValue() == highestFrequency && entry.getKey() < answer){
                answer = entry.getKey();
            }
        }
        pw.println(answer);
        br.close();
        pw.close();
    }
}
