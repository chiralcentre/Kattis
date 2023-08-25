import java.io.*;
import java.util.*;

class Point implements Comparable<Point> {// stores coordinates
    private double _first, _second;
  
    public Point(double f, double s) {
      _first = f;
      _second = s;
    }
  
    public int compareTo(Point o) {
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

public class humancannonball {
    public static double distance(double x1, double y1, double x2, double y2){
        return Math.sqrt(Math.pow(x1-x2,2) + Math.pow(y1-y2, 2)); //calculate Euclidean distance
    }
    
    public static double shortestTime(int u, int v, int n, Point[] p){
        Point s = p[u], e = p[v];
        double x1 = s.first(), y1 = s.second(), x2 = e.first(), y2 = e.second();
        double D = distance(x1, y1, x2, y2);
        // condition of 1 <= u <= n checks if starting point is a cannon 
        return u >= 1 && u <= n ? Math.min(2 + Math.abs((50-D)/5), D/5) : D/5;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" "), secondLine = br.readLine().split(" ");
        Point start = new Point(Double.parseDouble(firstLine[0]), Double.parseDouble(firstLine[1]));
        Point end = new Point(Double.parseDouble(secondLine[0]), Double.parseDouble(secondLine[1]));
        int INF = 1000000000, n = Integer.parseInt(br.readLine()); //use 1 billion to represent infinity
        Point[] p = new Point[n+2]; p[0] = start; // place start point at 0 index
        for (int i = 1; i < n+1; i++){
            String[] line = br.readLine().split(" ");
            p[i] = new Point(Double.parseDouble(line[0]), Double.parseDouble(line[1])); //add cannons
        }
        p[n+1] = end; //place endpoint at n+1 index
        double[] T = new double[n+2];
        for (int i = 1; i < n+2; i++) T[i] = INF; //initialisation, T[0] remains as 0
        PriorityQueue<DoubleIntPair> pq = new PriorityQueue<>(); // modified Djikstra's is used
        pq.offer(new DoubleIntPair(0, 0));
        while (!pq.isEmpty()){
            DoubleIntPair pair = pq.poll();
            double t = pair.first(); int u = pair.second();
            if (t == T[u]){// important check due to lazy DS
                for (int v = 0; v < n+2; v++){
                    if (u != v){
                        double edgeWeight = shortestTime(u,v,n,p); //edge weight represents shortest time taken to get from u to v
                        if (T[v] > T[u] + edgeWeight){
                            T[v] = T[u] + edgeWeight;
                            pq.offer(new DoubleIntPair(T[v], v));
                        }
                    }
                }
            }
        }
        pw.println(T[n+1]);
        br.close();
        pw.close();
    }
}
