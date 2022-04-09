import java.io.*;
import java.util.*;

class DoublePair implements Comparable<DoublePair> {// stores coordinates
    private double _first, _second;
  
    public DoublePair(double f, double s) {
      _first = f;
      _second = s;
    }
  
    public int compareTo(DoublePair o) {
      if (Double.compare(this.first(),o.first()) != 0) return Double.compare(this.first(),o.first());
      else return Double.compare(this.second(),o.second());
    }
  
    public double first() {return _first;}
  
    public double second() {return _second;}
}

class DoubleIntPair implements Comparable<DoubleIntPair> {// stores coordinates
    private double _first;
    private int _second;
  
    public DoubleIntPair(double f, int s) {
      _first = f;
      _second = s;
    }
  
    public int compareTo(DoubleIntPair o) {
      if (Double.compare(this.first(),o.first()) != 0) return Double.compare(this.first(),o.first());
      else return this.second() - o.second();
    }
  
    public double first() {return _first;}
  
    public int second() {return _second;}
}

public class arcticnetwork {
    public static double distance(double x1, double y1, double x2, double y2){
        return Math.sqrt(Math.pow(x1-x2,2) + Math.pow(y1-y2, 2)); //calculate Euclidean distance
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        double INF = 1000000000; // use 1 billion to represent infinity
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++){ // use Prim's variant for dense graphs with O(P^2) time complexity
            String[] L = br.readLine().split(" ");
            int S = Integer.parseInt(L[0]), P = Integer.parseInt(L[1]);
            DoublePair[] points = new DoublePair[P];
            DoubleIntPair[] A = new DoubleIntPair[P];
            for (int j = 0; j < P; j++) {
                String[] line = br.readLine().split(" ");
                points[j] = new DoublePair(Double.parseDouble(line[0]), Double.parseDouble(line[1]));
                A[j] = new DoubleIntPair(INF, j); // initialisation
            }
            boolean[] taken = new boolean[P];
            taken[0] = true; A[0] = new DoubleIntPair(0, 0);
            PriorityQueue<Double> cost = new PriorityQueue<Double>(Comparator.reverseOrder()); // turn it into maxHeap; cost keeps track of all edge weights in MST
            int counter = 1;  // counter keeps track of number of vertices in taken set to true
            while (counter < P){ // while not all vertices are in MST
                double lowest = INF; int v = 0; //scan A to get v where A[v].first is minimum in A
                for (int j = 0; j < P; j++){
                    if (A[j].first() < lowest){
                        lowest = A[j].first();
                        v = j;
                    }
                }
                if (!taken[v]) {counter += 1; taken[v] = true;}
                if (!taken[A[v].second()]) {counter += 1; taken[A[v].second()] = true;}
                cost.offer(A[v].first());
                A[v] = new DoubleIntPair(INF, A[v].second()); //prevent picking the same point
                for (int j = 0; j < P; j++){
                    if (!taken[j] && A[j].first() > distance(points[v].first(), points[v].second(), points[j].first(), points[j].second())){
                        A[j] = new DoubleIntPair(distance(points[v].first(), points[v].second(), points[j].first(), points[j].second()), v);
                    }
                }
            }
            for (int j = 0; j < S - 1; j++) {cost.poll();} // with S channels, there can be S - 1 edges. Remove the S-1 edges with the largest weights.
            pw.printf("%.2f%n",cost.peek()); //all remaining edges will have weights < largest edge in PQ
        }
        br.close();
        pw.close();
    }
}
