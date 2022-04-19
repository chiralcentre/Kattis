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

class IntegerTriple implements Comparable<IntegerTriple> {// first stores D[x][y],second and third stores x and y coordinates
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

public class blockcrusher {
    public static boolean inRange(int a, int b, int c){
        return c >= a && c <= b ? true : false;
    }

    public static ArrayList<IntegerPair> possiblepositions(int i, int j, int r, int c){
        int[][] movements = {{-1,0},{0,1},{1,0},{0,-1},{-1,-1},{-1,1},{1,-1},{1,1}}; // up,down,left,right and diagonals
        ArrayList<IntegerPair> neighbours = new ArrayList<IntegerPair>();
        for (int k = 0; k < 8; k++){
            if (inRange(0, r-1, i + movements[k][0]) && inRange(0, c-1, j + movements[k][1])){
                neighbours.add(new IntegerPair(i + movements[k][0], j + movements[k][1]));
            }
        }
        return neighbours;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int INF = 1000000000; // use 1 billion to represent infinity
        while (true){
            String[] dimensions = br.readLine().split(" ");
            int h = Integer.parseInt(dimensions[0]), w = Integer.parseInt(dimensions[1]); // h is number of rows, w is number of columns
            if (h == 0 && w == 0) break;
            ArrayList<String[]> board = new ArrayList<>();
            for (int i = 0; i < h; i++){ // storing board information
                String[] row = br.readLine().strip().split("");
                board.add(row);
            }
            int[][] D = new int[h][w]; IntegerPair[][] p = new IntegerPair[h][w]; // p stores parent of each cell
            PriorityQueue<IntegerTriple> PQ = new PriorityQueue<>();
            for (int j = 0; j < w; j++) { 
                D[0][j] = Integer.parseInt(board.get(0)[j]);
                p[0][j] = new IntegerPair(0, j);
                PQ.offer(new IntegerTriple(D[0][j], 0, j));
            }
            for (int i = 1; i < h; i++){
                for (int j = 0; j < w; j++){
                    D[i][j] = INF;
                }
            }
            // modified Djikstra's is used with O(hw log hw) time complexity
            while (!PQ.isEmpty()){
                IntegerTriple t = PQ.poll();
                int d = t.first(), i = t.second(), j = t.third();
                if (d == D[i][j]){ //check if this is the updated copy
                    for (IntegerPair neighbour: possiblepositions(i, j, h, w)){
                        int x = neighbour.first(), y = neighbour.second();
                        if (D[x][y] > D[i][j] + Integer.parseInt(board.get(x)[y])){//can be relaxed
                            D[x][y] = D[i][j] + Integer.parseInt(board.get(x)[y]);
                            p[x][y] = new IntegerPair(i, j);
                            PQ.offer(new IntegerTriple(D[x][y], x, y));
                        }
                    }
                }
            }
            // find fracture line with minimum strength in O(w) time
            // D[i][j] stores minimum strength of fracture line from top edge to board[i][j]
            int lowest = INF, idx = 0;
            for (int k = 0; k < w; k++){
                if (D[h-1][k] < lowest){
                    lowest = D[h-1][k];
                    idx = k;
                }
            }
            // backtrack with O(h) time complexity
            int x = h - 1, y = idx;
            while (p[x][y].first() != x || p[x][y].second() != y){
                board.get(x)[y] = " ";
                IntegerPair pair = p[x][y];
                x = pair.first(); y = pair.second();
            }
            board.get(x)[y] = " ";
            for (int i = 0; i < h; i++){
                String row = String.join("",board.get(i));
                pw.println(row);
            }
            pw.println(); //print new line
        }
        br.close();
        pw.close();
    }
}
