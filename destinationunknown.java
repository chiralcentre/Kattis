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

class IntegerPair implements Comparable<IntegerPair> {// first stores edge weight,second and third stores x and y coordinates
    private int first;
    private int second;

    public IntegerPair(int first, int second) {
        this.first = first;
        this.second = second;
    }
  
    public int compareTo(IntegerPair pair) {
        if (this.first - pair.first !=  0) return this.first - pair.first;
        else return this.second - pair.second;
    }
  
    public int getFirst() {return this.first;}
  
    public int getSecond() {return this.second;}
}


public class destinationunknown {
    static int INF = 1000000000;

    public static int[] modifiedDjikstra(ArrayList<ArrayList<Edge>> adjList, int n, int start) {
        //D[e] represents shortest distance from start to e
        int[] D = new int[n];
        for (int i = 0; i < n; i++) D[i] = INF;
        D[start] = 0;
        PriorityQueue<IntegerPair> PQ =  new PriorityQueue<>();
        PQ.add(new IntegerPair(0, start));
        while (!PQ.isEmpty()) {
            IntegerPair pair = PQ.poll();
            int d = pair.getFirst(), u = pair.getSecond();
            if (d == D[u]) {
                for (Edge e: adjList.get(u)) {
                    int v = e.getVertex(), w = e.getWeight();
                    if (D[v] > D[u] + w) {
                        D[v] = D[u] + w;
                        PQ.add(new IntegerPair(D[v], v));
                    }
                }
            }
        }
        return D;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int T = Integer.parseInt(br.readLine());
        for (int k = 0; k < T; k++) {
            String[] firstLine = br.readLine().split(" "), secondLine = br.readLine().split(" ");
            int n = Integer.parseInt(firstLine[0]), m = Integer.parseInt(firstLine[1]), t = Integer.parseInt(firstLine[2]);
            int s = Integer.parseInt(secondLine[0]), g = Integer.parseInt(secondLine[1]), h = Integer.parseInt(secondLine[2]);
            s--; g--; h--; //offset by 1 due to zero indexing
            ArrayList<ArrayList<Edge>> adjList = new ArrayList<>();
            for (int i = 0; i < n; i++) adjList.add(new ArrayList<>());
            for (int i = 0; i < m; i++) {
                String[] line = br.readLine().split(" ");
                int u = Integer.parseInt(line[0]), v = Integer.parseInt(line[1]), w = Integer.parseInt(line[2]);
                u--; v--; //offset bu 1 due to zero indexing
                adjList.get(u).add(new Edge(v, w));
                adjList.get(v).add(new Edge(u, w));
            }
            int[] destinations = new int[t];
            for (int i = 0; i < t; i++) destinations[i] = Integer.parseInt(br.readLine()) - 1; //offset by 1 due to zero indexing
            Arrays.sort(destinations);
            int[] Ds = modifiedDjikstra(adjList, n, s);
            int[] Dg = modifiedDjikstra(adjList, n, g);
            int[] Dh = modifiedDjikstra(adjList, n, h);
            ArrayList<Integer> answer = new ArrayList<>();
            for (int p: destinations) {
                if (Ds[g] + Dg[h] + Dh[p] == Ds[p] || Ds[h] + Dh[g] + Dg[p] == Ds[p]) {
                    answer.add(p);
                }
            }
            Collections.sort(answer);
            for (int i = 0; i < answer.size(); i++) {
                if (i > 0) pw.print(" ");
                pw.print(answer.get(i) + 1); //add back 1 to negate zero indexing offset
            }
            pw.print("\n");
        }
        br.close();
        pw.close();
    }
}
