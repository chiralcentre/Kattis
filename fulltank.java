import java.io.*;
import java.util.*;

class Edge implements Comparable<Edge> {// stores coordinates
    private int v;
    private int w;
  
    public Edge(int v, int w) {
        this.v = v;
        this.w = w;
    }
  
    public int compareTo(Edge edge) {
        if (this.w - edge.w !=  0) return this.w - edge.w;
        else return this.v - edge.v;
    }
  
    public int getVertex() {return this.v;}
  
    public int getWeight() {return this.w;}
}

class IntegerTriple implements Comparable<IntegerTriple> {// first stores edge weight,second and third stores x and y coordinates
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

public class fulltank {
    static int INF = 1000000000;

    public static String modifiedDjikstra(int c, int s, int e, int n, int[] fuelPrices, ArrayList<ArrayList<Edge>> adjList) {
        if (s == e) return "0"; //no fuel required
        int[][] P = new int[n][c + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < c + 1; j++) {
                P[i][j] = INF;
            }
        }
        P[s][0] = 0; PriorityQueue<IntegerTriple> PQ = new PriorityQueue<>();
        PQ.offer(new IntegerTriple(0, s, 0));
        while (!PQ.isEmpty()) {
            IntegerTriple temp = PQ.poll();
            int cost = temp.first(), u = temp.second(), f = temp.third();
            if (u == e) { // end city is reached and lowest cost is attained
                return String.format("%d",cost);
            }
            if (cost == P[u][f]) {
                //refueling 1 unit of fuel at u
                if (f < c && P[u][f + 1] > cost + fuelPrices[u]) {
                    P[u][f + 1] = cost + fuelPrices[u];
                    PQ.offer(new IntegerTriple(P[u][f + 1], u, f + 1));
                } 
                for (Edge edge: adjList.get(u)) {
                    int v = edge.getVertex(), w = edge.getWeight();
                    // fuel >= distance, no additional cost required
                    if (f >= w && P[v][f - w] > P[u][f]) {
                        P[v][f - w] = P[u][f];
                        PQ.offer(new IntegerTriple(P[v][f - w], v, f - w));
                    }
                }
            }
        }
        return "impossible";
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine =  br.readLine().split(" ");
        int n =  Integer.parseInt(firstLine[0]), m = Integer.parseInt(firstLine[1]);
        ArrayList<ArrayList<Edge>> adjList =  new ArrayList<>();
        String[] secondLine = br.readLine().split(" ");
        int[] fuelPrices = new int[n];
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<Edge>());
            fuelPrices[i] = Integer.parseInt(secondLine[i]);
        }
        for (int i = 0; i < m; i++) {
            String[] line =  br.readLine().split(" ");
            int u = Integer.parseInt(line[0]), v = Integer.parseInt(line[1]), w = Integer.parseInt(line[2]);
            adjList.get(u).add(new Edge(v,w));
            adjList.get(v).add(new Edge(u,w));
        }
        int q = Integer.parseInt(br.readLine());
        for (int i = 0; i < q; i++) {
            String[] query = br.readLine().split(" ");
            int c = Integer.parseInt(query[0]), s = Integer.parseInt(query[1]), e = Integer.parseInt(query[2]);
            pw.printf("%s\n",modifiedDjikstra(c,s,e,n,fuelPrices,adjList));
        }
        br.close();
        pw.close();
    }
}
