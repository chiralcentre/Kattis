import java.io.*;
import java.util.*;

class Delivery {
    private int time;
    private int money;

    public Delivery(int time, int money) {
        this.time = time;
        this.money = money;
    }

    public int getTime() {return this.time;}

    public int getMoney() {return this.money;}
}

public class profitablepizzas {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        //maximum revenue is 2*10^7
        int N = Integer.parseInt(br.readLine()), highestTime = -1, revenue = 0;
        Delivery[] deliveryList = new Delivery[N];
        for (int i = 0; i < N; i++){
            String[] line = br.readLine().split(" ");
            int t = Integer.parseInt(line[0]), c = Integer.parseInt(line[1]);
            deliveryList[i] = new Delivery(t, c);
            if (t > highestTime) highestTime = t;
        }
        //timeslots[a] contains the deliveries made at time a
        ArrayList<ArrayList<Integer>> timeslots = new ArrayList<>();
        for (int i = 0; i < highestTime; i++) timeslots.add(new ArrayList<Integer>());
        for (Delivery d : deliveryList) timeslots.get(d.getTime() - 1).add(d.getMoney());
        //a max heap is used
        PriorityQueue<Integer> deliveries = new PriorityQueue<>(Collections.reverseOrder());
        //start from the highest timeslot as customers can be served at any time before that
        //time complexity is O(N + N log N) since a maximum of N deliveries can be made
        for (int i = highestTime - 1; i > -1; i--) {
            for (int r: timeslots.get(i)) deliveries.add(r);
            if (deliveries.size() > 0) revenue += deliveries.poll();
        }
        pw.println(revenue);
        br.close();
        pw.close();
    }
}
