import java.io.*;

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

public class islandhopping {
    public static double distance(double x1, double y1, double x2, double y2){
        return Math.sqrt(Math.pow(x1-x2,2) + Math.pow(y1-y2, 2)); //calculate Euclidean distance
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        double INF = 1000000000; // use 1 billion to represent infinity
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++){ // use Prim's variant for dense graphs with O(m^2) time complexity
            int m = Integer.parseInt(br.readLine());
            DoublePair[] points = new DoublePair[m];
            DoubleIntPair[] A = new DoubleIntPair[m];
            for (int j = 0; j < m; j++) {
                String[] line = br.readLine().split(" ");
                points[j] = new DoublePair(Double.parseDouble(line[0]), Double.parseDouble(line[1]));
                A[j] = new DoubleIntPair(INF, j); // initialisation
            }
            boolean[] taken = new boolean[m];
            taken[0] = true; A[0] = new DoubleIntPair(0, 0);
            double cost = 0, counter = 1; // cost keeps track of total edge weights in MST, while counter keeps track of number of vertices in taken set to true
            while (counter < m){ // while not all vertices are in MST
                double lowest = INF; int v = 0; //scan A to get v where A[v].first is minimum in A
                for (int j = 0; j < m; j++){
                    if (A[j].first() < lowest){
                        lowest = A[j].first();
                        v = j;
                    }
                }
                if (!taken[v]) {counter += 1; taken[v] = true;}
                if (!taken[A[v].second()]) {counter += 1; taken[A[v].second()] = true;}
                cost += A[v].first();
                A[v] = new DoubleIntPair(INF, A[v].second()); //prevent picking the same point
                for (int j = 0; j < m; j++){
                    if (!taken[j] && A[j].first() > distance(points[v].first(), points[v].second(), points[j].first(), points[j].second())){
                        A[j] = new DoubleIntPair(distance(points[v].first(), points[v].second(), points[j].first(), points[j].second()), v);
                    }
                }
            }
            pw.println(cost);
        }
        br.close();
        pw.close();
    }
}
