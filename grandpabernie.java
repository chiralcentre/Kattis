import java.io.*;
import java.util.*;

public class grandpabernie{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = Integer.parseInt(br.readLine());
        HashMap<String,ArrayList<Integer>> tripRecord = new HashMap<>();
        for (int i = 0; i < n; i++){
            String[] line = br.readLine().split(" "); // line[0] contains the country, line[1] contains the year
            int year = Integer.parseInt(line[1]);
            if (tripRecord.containsKey(line[0])){tripRecord.get(line[0]).add(year);} //pass by reference
            else {tripRecord.put(line[0], new ArrayList<Integer>(){{add(year);}});}
        }
        for (String key: tripRecord.keySet()){Collections.sort(tripRecord.get(key));} // sort the trip years in ascending order
        int q = Integer.parseInt(br.readLine());
        for (int i = 0; i < q; i++){
            String[] line = br.readLine().split(" ");
            pw.println(tripRecord.get(line[0]).get(Integer.parseInt(line[1])-1)); // -1 due to zero indexing
        }
        br.close();
        pw.close();
    }
}