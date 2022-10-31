import java.io.*;
import java.util.*;

class Pair {
    private int first;
    private int second;
  
    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }

    public int getFirst() {return this.first;}

    public int getSecond() {return this.second;}
}

class Edge implements Comparable<Edge> {// stores coordinates
    private int v;
    private int w;
    private int r;
  
    public Edge(int v, int w, int r) {
        this.v = v;
        this.w = w;
        this.r = r;
    }
  
    public int compareTo(Edge edge) {
        if (this.w - edge.w !=  0) return this.w - edge.w;
        else return this.v - edge.v;
    }
  
    public int getVertex() {return this.v;}
  
    public int getWeight() {return this.w;}

    public int getRoad() {return this.r;}
}

class VertexEdgePair implements Comparable<VertexEdgePair> {// stores coordinates
    private int u;
    private Edge e;
  
    public VertexEdgePair(int u, Edge e) {
        this.u = u;
        this.e = e;
    }
  
    public int compareTo(VertexEdgePair p) {
        if (this.e.getWeight() - p.e.getWeight() !=  0) return this.e.getWeight() - p.e.getWeight();
        else return this.u - p.u;
    }
  
    public int getVertex() {return this.u;}
  
    public Edge getEdge() {return this.e;}
}

//Approach:
//use Prim's to form a maximum spanning tree
//remove all streets incident to vertices on the maximin path from vertex 0 to vertex m - 1 in the maxST
public class crowdcontrol {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]), m = Integer.parseInt(firstLine[1]);
        ArrayList<ArrayList<Edge>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) adjList.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            String[] line = br.readLine().split(" ");
            int u = Integer.parseInt(line[0]), v = Integer.parseInt(line[1]), w = Integer.parseInt(line[2]);
            adjList.get(u).add(new Edge(v, w, i));
            adjList.get(v).add(new Edge(u, w, i));
        }
        //start from vertex 0, the train station
        boolean[] taken = new boolean[n]; taken[0] = true;
        PriorityQueue<VertexEdgePair> PQ = new PriorityQueue<>(Collections.reverseOrder());
        for (Edge e: adjList.get(0)) PQ.add(new VertexEdgePair(0, e));
        // perform Prim's algorithm in O(m log m) time
        Pair[] parent = new Pair[n];
        for (int i = 0; i < n; i++) {
            parent[i] = new Pair(-1,-1);
        }
        // E keeps track of number of edges
        int E = 0;
        while (!PQ.isEmpty()) {
            VertexEdgePair pair = PQ.poll();
            int p = pair.getVertex(); Edge e = pair.getEdge();
            int u = e.getVertex(); int r = e.getRoad();
            if (!taken[u]) {
                taken[u] = true; parent[u] = new Pair(p,r);
                if (E == n - 1) break; //full maxST is formed
                for (Edge adjEdge: adjList.get(u)) {
                    if (!taken[adjEdge.getVertex()]) {
                        PQ.add(new VertexEdgePair(u, adjEdge));
                    }
                }
            }
        }
        //maximinVertices stores the vertices on the maximin path from vertex 0 to vertex n - 1
        //maximinPath stores the numbers of the streets on the maximin path from vertex 0 to vertex n - 1
        //perform backtracking 
        ArrayList<Integer> maximinVertices = new ArrayList<>();
        HashSet<Integer> maximinPath = new HashSet<>();
        int start = n - 1; maximinVertices.add(n - 1);
        while (parent[start].getFirst() != - 1) {
            Pair p = parent[start];
            start = p.getFirst(); int r = p.getSecond();
            maximinVertices.add(start);
            maximinPath.add(r);
        }
        //remove all streets incident to vertices on the maximin path from vertex 0 to vertex m - 1 in the maxST
        HashSet<Integer> blockedStreets = new HashSet<>(); // set is used to prevent duplicates
        for (int u: maximinVertices) {
            for (Edge e: adjList.get(u)) {
                if (!maximinPath.contains(e.getRoad())) { //can remove street from usage
                    blockedStreets.add(e.getRoad());
                }
            }
        }
        ArrayList<Integer> answer =  new ArrayList<>(blockedStreets);
        Collections.sort(answer);
        if (answer.size() == 0) {
            pw.print("none\n");
        } else {
            for (int i = 0; i < answer.size(); i++) {
                if (i > 0) pw.print(" ");
                pw.print(answer.get(i));
            }
            pw.print("\n");
        }
        br.close();
        pw.close();
    }
}
