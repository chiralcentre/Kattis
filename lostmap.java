import java.io.*;
import java.util.*;

class UnionFind {                                              
    public int[] p;
    public int[] rank;

    public UnionFind(int N) {
        p = new int[N];
        rank = new int[N];
        for (int i = 0; i < N; i++) {
            p[i] = i;
            rank[i] = 0;
        }
    }

    public int findSet(int i) { 
        if (p[i] == i) return i;
        else {
            p[i] = findSet(p[i]);
            return p[i]; 
        } 
    }

    public Boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

    public void unionSet(int i, int j) { 
        if (!isSameSet(i, j)) { 
            int x = findSet(i), y = findSet(j);
            if (rank[x] > rank[y]) 
                p[y] = x;
            else { 
                p[x] = y;
                if (rank[x] == rank[y]) 
                rank[y] = rank[y]+1; 
            } 
        } 
    }
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

public class lostmap{   
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine()), E = 0;
        ArrayList<IntegerTriple> edgeList = new ArrayList<>();
        for (int i = 0; i < N; i++){
            String[] row = br.readLine().split(" ");
            for (int j = i+1; j < N; j++) {//only need to consider one half due to symmetry
                edgeList.add(new IntegerTriple(Integer.parseInt(row[j]), i, j));
            }
        }
        // use Kruskal's
        Collections.sort(edgeList);
        UnionFind disjointSets = new UnionFind(N);
        for (IntegerTriple edge: edgeList){
            int u = edge.second(), v = edge.third();
            if (E == N - 1) {break;} // all MST edges are found
            if (!disjointSets.isSameSet(u, v)){
                disjointSets.unionSet(u, v); E += 1;
                pw.printf("%d %d%n",u+1,v+1); //print out edges as Kruskal's is being run
            }
        }
        br.close();
        pw.close();
    }
}