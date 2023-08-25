import java.io.*;
import java.util.*;

public class workstations {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]), m = Integer.parseInt(firstLine[1]), saves = 0;
        // One array for arrival timings, and one PQ for departure timings
        PriorityQueue<Integer> departures = new PriorityQueue<Integer>();
        int[] arrivals = new int[n];
        for (int i = 0; i < n; i++){
            String[] line = br.readLine().split(" ");
            int a = Integer.parseInt(line[0]), s = Integer.parseInt(line[1]);
            arrivals[i] = a;
            departures.add(a+s);
        }
        Arrays.sort(arrivals); // sort arrivals in ascending order
        for (int j = 0; j < n; j++){
            // if earliest arrival time is more than earliest departure time by m minutes, the computer will be locked
            // no saves are made, and a manual unlock will have to be done
            while (arrivals[j] - departures.peek() > m){departures.remove();}
            // if a researcher arrives after another one has left, and before m minutes has elapsed, a save is made
            if (arrivals[j]>= departures.peek()){
                departures.remove();
                saves += 1;
            }
        }
        pw.println(saves);
        br.close();
        pw.close();
    }
}
