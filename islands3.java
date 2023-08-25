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

public class islands3 {
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

    public static void DFS(int i, int j, int r, int c, String[] grid, boolean[][] visited){// iterative version of DFS
        Stack <IntegerPair> frontier = new Stack<>();
        frontier.push(new IntegerPair(i,j)); visited[i][j] = true;
        while (!frontier.empty()){
            IntegerPair point = frontier.pop();
            int x = point.first(), y = point.second();
            for (IntegerPair p: possiblepositions(x,y,r,c)){
                int a = p.first(), b = p.second();
                if (!visited[a][b] && (grid[a].charAt(b) == 'L' || grid[a].charAt(b) == 'C')){// if neighbouring cell is land or cloud, extend the island
                    visited[a][b] = true;
                    frontier.push(new IntegerPair(a, b));
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int r = Integer.parseInt(firstLine[0]), c = Integer.parseInt(firstLine[1]), islands = 0;
        String[] grid = new String[r];
        for (int i = 0; i < r; i++) {grid[i] = br.readLine().strip();}
        boolean[][] visited = new boolean[r][c]; // boolean array initialised to false
        // this problem is equivalent to finding minimum number of components containing land or cloud cells
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                if (grid[i].charAt(j) == 'L' && !visited[i][j]){// current cell unvisited and current cell is a piece of land
                    islands++;
                    DFS(i,j,r,c,grid,visited);
                }
            }
        }
        pw.println(islands);
        br.close();
        pw.close();
    }
}
