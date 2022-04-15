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

public class fire3 {
    public static boolean inRange(int a, int b, int c){
        return c >= a && c <= b ? true : false;
    }

    public static ArrayList<IntegerPair> possiblepositions(int i, int j, int r, int c, String[] grid){
        int[][] movements = {{-1,0},{0,1},{1,0},{0,-1}};
        ArrayList<IntegerPair> neighbours = new ArrayList<IntegerPair>();
        for (int k = 0; k < 4; k++){
            if (inRange(0, r-1, i + movements[k][0]) && inRange(0, c-1, j + movements[k][1]) && grid[i + movements[k][0]].charAt(j + movements[k][1]) != '#'){
                neighbours.add(new IntegerPair(i + movements[k][0], j + movements[k][1]));
            }
        }
        return neighbours;
    }

    public static String solution (int r, int c, String[] grid){
        boolean[][] visited = new boolean[r][c];
        Queue<IntegerPair> frontierJoe = new LinkedList<IntegerPair>(), frontierFire = new LinkedList<IntegerPair>();
        for (int i = 0; i < r; i++){ // initialisation of queues for BFS
            for (int j = 0; j < c; j++){
                if (grid[i].charAt(j) == 'J') {
                    if ( i == 0 || i == r - 1 || j == 0 || j == c - 1) return "1"; // only one move needed to move out of border
                    visited[i][j] = true;
                    frontierJoe.offer(new IntegerPair(i, j));
                }
                if (grid[i].charAt(j) == 'F'){
                    visited[i][j] = true;
                    frontierFire.offer(new IntegerPair(i, j));
                }
            }
        }
        int time = 0;
        while (!frontierJoe.isEmpty()){// go round by round
            time++;
            Queue<IntegerPair> newfrontierJoe = new LinkedList<IntegerPair>(), newfrontierFire = new LinkedList<IntegerPair>();
            for (IntegerPair f: frontierFire){// simulate fire spread
                for (IntegerPair neighbour: possiblepositions(f.first(), f.second(), r, c, grid)){
                    int i = neighbour.first(), j = neighbour.second();
                    if (!visited[i][j]){
                        visited[i][j] = true;
                        newfrontierFire.offer(new IntegerPair(i, j));
                    }
                }
            }
            for (IntegerPair u: frontierJoe){ // simulate possible movements of Joe
                for (IntegerPair v: possiblepositions(u.first(), u.second(), r, c, grid)){
                    int i = v.first(), j = v.second();
                    if (!visited[i][j]){
                        if (i == 0 || i == r - 1 || j == 0 || j == c - 1) return Integer.toString(time + 1); // +1 since one more move needed to go out
                        visited[i][j] = true;
                        newfrontierJoe.offer(new IntegerPair(i, j));
                    }
                }
            }
            frontierJoe = newfrontierJoe; frontierFire = newfrontierFire;
        }
        return "IMPOSSIBLE";
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int R = Integer.parseInt(firstLine[0]), C = Integer.parseInt(firstLine[1]);
        String[] grid = new String[R];
        for (int i = 0; i < R; i++) {grid[i] = br.readLine().strip();}
        pw.println(solution(R,C,grid));
        br.close();
        pw.close();
    }
}
