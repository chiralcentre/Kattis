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

class IntegerTriple implements Comparable<IntegerTriple> {// stores coordinates and number of moves
    private Integer _first, _second,_third;
  
    public IntegerTriple(Integer f, Integer s, Integer z) {
      _first = f;
      _second = s;
      _third = z;
    }
  
    public int compareTo(IntegerTriple o) {
      if (!this.first().equals(o.first())) return this.first() - o.first();
      else return this.second() - o.second();
    }
  
    Integer first() {return _first;}
  
    Integer second() {return _second;}

    Integer third() {return _third;}
}

public class grasshopper {
    public static boolean inRange(int a, int b, int c){
        return c >= a && c <= b ? true : false;
    }
    public static ArrayList<IntegerPair> possiblepositions(int i, int j, int r, int c){
        int[][] movements = {{2,1},{2,-1},{-2,1},{-2,-1},{1,2},{1,-2},{-1,2},{-1,-2}};
        ArrayList<IntegerPair> neighbours = new ArrayList<IntegerPair>();
        for (int k = 0; k < 8; k++){
            if (inRange(0,r-1,i + movements[k][0]) && inRange(0,c-1,j + movements[k][1])){
                neighbours.add(new IntegerPair(i + movements[k][0], j + movements[k][1]));
            }
        }
        return neighbours;
    }

    public static int BFS(int start_x,int start_y,int end_x,int end_y, int r, int c){
        if (start_x == end_x && start_y == end_y) return 0; // start and end positions are the same
        boolean[][] visited = new boolean[r][c]; // default value is false
        visited[start_x][start_y] = true;
        Queue<IntegerTriple> frontier = new ArrayDeque<IntegerTriple>(); //ArrayDeque is faster than LinkedList, according to online sources
        frontier.offer(new IntegerTriple(start_x,start_y,0));
        while (frontier.size() > 0){ //BFS
            IntegerTriple pos = frontier.poll();
            int i = pos.first(), j = pos.second(), counter = pos.third(); //third keeps track of number of moves made
            for (IntegerPair p: possiblepositions(i,j,r,c)){
                if (p.first() == end_x && p.second() == end_y) return counter + 1;
                if (!visited[p.first()][p.second()]){
                    visited[p.first()][p.second()] = true;
                    frontier.offer(new IntegerTriple(p.first(), p.second(), counter+1));
                }
            }
        }
        return -1; // impossible to reach end position
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        while (true){
            try {
                String[] line = br.readLine().split(" ");
                int R = Integer.parseInt(line[0]), C = Integer.parseInt(line[1]), Gr = Integer.parseInt(line[2]),
                Gc = Integer.parseInt(line[3]), Lr = Integer.parseInt(line[4]), Lc = Integer.parseInt(line[5]);
                Gr -= 1; Gc -= 1; Lr -= 1; Lc -= 1; //offset by 1 due to zero indexing
                int moves = BFS(Gr,Gc,Lr,Lc,R,C);
                pw.println(moves != -1 ? moves : "impossible");
            }
            catch (Exception e){ // check for EOF error
                break;
            }
        }
        br.close();
        pw.close();
    }
}
