import java.io.*;
import java.util.*;

class IntegerPair implements Comparable<IntegerPair> {// stores coordinates
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

public class millionairemadness {
    public static boolean inRange(int a, int b, int c){
        return c >= a && c <= b ? true : false;
    }

    public static ArrayList<IntegerPair> possiblepositions(int i, int j, int r, int c){// returns possible neighbours
        int[][] movements = {{-1,0},{1,0},{0,-1},{0,1}};
        ArrayList<IntegerPair> neighbours = new ArrayList<IntegerPair>();
        for (int k = 0; k < 4; k++){
            if (inRange(0,r-1,i + movements[k][0]) && inRange(0,c-1,j + movements[k][1])){
                neighbours.add(new IntegerPair(i + movements[k][0], j + movements[k][1]));
            }
        }
        return neighbours;
    }   

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int M = Integer.parseInt(firstLine[0]), N = Integer.parseInt(firstLine[1]);
        int[][] vault = new int[M][N];
        for (int i = 0; i < M; i++){
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < N; j++) vault[i][j] = Integer.parseInt(row[j]);
        }
        // problem is equivalent to finding minimax path from (0,0) to (M-1,N-1), which can be done by finding MST
        // Prim's algorithm is used here
        PriorityQueue <IntegerTriple> pq = new PriorityQueue<>();
        int largestEdgeWeight = 0; // keep track of largest edge weight(ladder height) in the process of finding MST
        boolean[][] taken = new boolean[M][N];
        pq.offer(new IntegerTriple(0, 0, 0)); // start from (0,0), edge weight of 0
        while (!pq.isEmpty()){
            IntegerTriple tuple = pq.poll();
            int w = tuple.first(), i = tuple.second(), j = tuple.third();
            if (!taken[i][j]){
                taken[i][j] = true;
                if (i == M - 1 & j == N -1) {break;} //end point is reached, no need to find full MST
                if (w > largestEdgeWeight) {largestEdgeWeight = w;}
                for (IntegerPair point: possiblepositions(i,j,M,N)){
                    int a = point.first(), b = point.second();
                    if (!taken[a][b]){
                        int weight = Math.max(vault[a][b] - vault[i][j],0); // ladder height cannot be negative
                        pq.offer(new IntegerTriple(weight,a,b));
                    }
                }
            }
        }
        pw.println(largestEdgeWeight);
        br.close();
        pw.close();
    }
}
