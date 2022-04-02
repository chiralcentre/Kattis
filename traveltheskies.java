import java.io.*;
import java.util.ArrayList;

class IntegerPair implements Comparable<IntegerPair> {// stores arrival details
    private Integer _first, _second;
  
    public IntegerPair(Integer f, Integer s) {
      _first = f;
      _second = s;
    }
  
    public int compareTo(IntegerPair o) {
      if (!this.first().equals(o.first())) return this.first() - o.first();
      else return this.second() - o.second();
    }
  
    Integer first() {return _first;}
  
    Integer second() {return _second;}
}

class IntegerTriple implements Comparable<IntegerTriple> {// first stores start point,second stores end point, third stores capacity
    private Integer _first, _second,_third;
  
    public IntegerTriple(Integer f, Integer s, Integer z) {
      _first = f;
      _second = s;
      _third = z;
    }
  
    public int compareTo(IntegerTriple o) {
      if (!this.first().equals(o.first())) return this.first() - o.first();
      else if (!this.second().equals(o.second())) return this.second() - o.second();
      else return this.third() - o.third();
    }
  
    Integer first() {return _first;}
  
    Integer second() {return _second;}

    Integer third() {return _third;}
}

public class traveltheskies{
    public static String optimalFlightPlan(int n, int k, ArrayList<ArrayList<IntegerTriple>> flights,int[] airports, ArrayList<ArrayList<IntegerPair>> arrivals){
        for (int d = 0; d < n; d++){
            for (IntegerPair p: arrivals.get(d)){airports[p.first()] += p.second();}
            //check if existing customers at airport are sufficient without transferring the customers yet
            //since every customer can only have one flight a day
            for (IntegerTriple t: flights.get(d)){
                int start = t.first(), capacity = t.third();
                if (airports[start] < capacity) return "suboptimal";
                else airports[start] -= capacity;
            }
            for (IntegerTriple t: flights.get(d)){ // for second iteration, update capacity at destination airport
                int end = t.second(), capacity = t.third();
                airports[end] += capacity;
            }
        }
        return "optimal";
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int k = Integer.parseInt(firstLine[0]), n = Integer.parseInt(firstLine[1]), m = Integer.parseInt(firstLine[2]);
        ArrayList<ArrayList<IntegerTriple>> flights = new ArrayList<>(); //store flights as edge list
        ArrayList<ArrayList<IntegerPair>> arrivals = new ArrayList<>();
        int[] airports = new int[k];
        for (int i = 0; i < n; i++){ //initialisation
            flights.add(new ArrayList<IntegerTriple>());
            arrivals.add(new ArrayList<IntegerPair>());
        }
        for (int i = 0; i < m; i++){
            String[] f = br.readLine().split(" ");
            int u = Integer.parseInt(f[0]) - 1, v = Integer.parseInt(f[1]) - 1, d = Integer.parseInt(f[2]) - 1, z = Integer.parseInt(f[3]); // offset by 1 due to zero indexing
            flights.get(d).add(new IntegerTriple(u, v, z));
        }
        for (int i = 0; i < k*n; i++){
            String[] f = br.readLine().split(" ");
            int a = Integer.parseInt(f[0]) - 1, b = Integer.parseInt(f[1]) - 1, c = Integer.parseInt(f[2]); // offset by 1 due to zero indexing
            arrivals.get(b).add(new IntegerPair(a, c));
        }
        pw.println(optimalFlightPlan(n,k,flights,airports,arrivals));
        br.close();
        pw.close();
    }
}