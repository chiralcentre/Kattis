import java.io.*;
import java.util.*;

public class profitablepizzas {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        //maximum revenue is 2*10^7
        int N = Integer.parseInt(br.readLine()), highestTime = -1, revenue = 0;
        //timeslots[a] contains the deliveries made at time a
        ArrayList<ArrayList<Integer>> timeslots = new ArrayList<>();
        //highest possible time is 2000000
        for (int i = 0; i < 2000000; i++) timeslots.add(new ArrayList<Integer>());
        for (int i = 0; i < N; i++){
            String[] line = br.readLine().split(" ");
            int t = Integer.parseInt(line[0]), c = Integer.parseInt(line[1]);
            if (t > highestTime) highestTime = t;
            timeslots.get(t-1).add(c);
        }
        //a max heap is used
        PriorityQueue<Integer> deliveries = new PriorityQueue<>(Collections.reverseOrder());
        //start from the highest timeslot as customers can be served at any time before that
        //time complexity is O(highestTime + N log N) since a maximum of N deliveries can be made
        for (int i = highestTime - 1; i > -1; i--) {
            for (int r: timeslots.get(i)) deliveries.add(r);
            if (deliveries.size() > 0) revenue += deliveries.poll();
        }
        pw.println(revenue);
        br.close();
        pw.close();
    }
}
