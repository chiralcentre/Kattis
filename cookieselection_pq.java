import java.util.*;
import java.io.*;

public class cookieselection_pq {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        PriorityQueue<Integer> maxpq = new PriorityQueue<Integer>(Collections.reverseOrder()); //stores smaller half of numbers
        PriorityQueue<Integer> minpq = new PriorityQueue<Integer>(); //stores the largest half of the numbers
        String line = null;
        while ((line = br.readLine()) != null){// take in input until EOF
            line = line.strip();
            if (line.equals("#")){
                int m = minpq.poll();
                if (minpq.size() != maxpq.size()) {
                    minpq.add(maxpq.poll());  
                }
                pw.println(m);
            }
            else {
                int d = Integer.parseInt(line);
                if (minpq.size() == 0 || d > minpq.peek()) {
                    minpq.add(d);
                    if (minpq.size() > maxpq.size() + 1) {
                        maxpq.add(minpq.poll());
                    }
                }
                else {
                    maxpq.add(d);
                    if (maxpq.size() > minpq.size()) {
                        minpq.add(maxpq.poll());
                    }
                }
            }
        }
        br.close();
        pw.close();
    }
}