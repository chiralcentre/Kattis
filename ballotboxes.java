import java.io.*;
import java.util.*;

class City implements Comparable<City>{
    public double voters,boxes;

    public City(double voters, double boxes){
        this.voters = voters;
        this.boxes = boxes;
    }

    public int compareTo(City c) {return Double.compare(this.voters, c.voters);}

}
public class ballotboxes {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        while (true){
            String[] firstLine = br.readLine().split(" ");
            double N = Double.parseDouble(firstLine[0]), B = Double.parseDouble(firstLine[1]);
            if (N == -1 && B == -1) {break;}
            PriorityQueue<City> cities = new PriorityQueue<City>(Comparator.reverseOrder()); // turn it into maxHeap
            for (int i = 0; i < N; i++) {cities.add(new City(Double.parseDouble(br.readLine()),1));}
            for (int j = 0; j < B - N; j++){
                City c = cities.poll();
                double v = c.voters, b = c.boxes;
                cities.add(new City((v*b/(b+1)),b+1));
            }
            String blankLine = br.readLine();
            pw.println((int) Math.ceil(cities.poll().voters));
        }
        br.close();
        pw.close();
    }
}
