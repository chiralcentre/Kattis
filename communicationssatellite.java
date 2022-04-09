import java.io.*;

class Circle implements Comparable<Circle> {// stores coordinates
    private double _first, _second,_third;
  
    public Circle(double f, double s, double t) {
        _first = f;
        _second = s;
        _third = t;
    }
  
    public int compareTo(Circle o) {
      if (Double.compare(this.x(),o.x()) != 0) return Double.compare(this.x(),o.x());
      else if (Double.compare(this.y(),o.y()) != 0) return Double.compare(this.y(),o.y());
      else return Double.compare(this.radius(),o.radius());
    }
  
    public double x() {return _first;}
  
    public double y() {return _second;}

    public double radius() {return _third;}
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

public class communicationssatellite {
    public static double distance(double x1, double y1, double x2, double y2){
        return Math.sqrt(Math.pow(x1-x2,2) + Math.pow(y1-y2, 2)); //calculate Euclidean distance
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        double INF = 1000000000; // use 1 billion to represent infinity
        int n = Integer.parseInt(br.readLine());
        Circle[] points = new Circle[n]; // use Prim's variant for dense graphs with O(n^2) time complexity
        DoubleIntPair[] A = new DoubleIntPair[n];
        for (int j = 0; j < n; j++) {
            String[] line = br.readLine().split(" ");
            points[j] = new Circle(Double.parseDouble(line[0]), Double.parseDouble(line[1]),Double.parseDouble(line[2]));
            A[j] = new DoubleIntPair(INF, j); // initialisation
        }
        boolean[] taken = new boolean[n];
        taken[0] = true; A[0] = new DoubleIntPair(0, 0);
        double cost = 0; int counter = 1; // cost keeps track of total edge weights in MST, while counter keeps track of number of vertices in taken set to true
        while (counter < n){ // while not all vertices are in MST
            double lowest = INF; int v = 0; //scan A to get v where A[v].first is minimum in A
            for (int j = 0; j < n; j++){
                if (A[j].first() < lowest){
                    lowest = A[j].first();
                    v = j;
                }
            }
            if (!taken[v]) {counter += 1; taken[v] = true;}
            if (!taken[A[v].second()]) {counter += 1; taken[A[v].second()] = true;}
            cost += A[v].first();
            A[v] = new DoubleIntPair(INF, A[v].second()); //prevent picking the same point
            for (int j = 0; j < n; j++){
                if (!taken[j] && A[j].first() > distance(points[v].x(), points[v].y(), points[j].x(), points[j].y()) - points[v].radius() - points[j].radius()){ //subtract radius of two circles from distance between their two centres
                    A[j] = new DoubleIntPair(distance(points[v].x(), points[v].y(), points[j].x(), points[j].y()) - points[v].radius() - points[j].radius(), v);
                }
            }
        }
        pw.println(cost);
        br.close();
        pw.close();
    }
}