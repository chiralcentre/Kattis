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

public class onepunch {
    public static int[][] movements = {{-1,0},{1,0},{0,-1},{0,1}};

    public static boolean inRange(int a, int b, int c){
        return c >= a && c <= b ? true : false;
    }

    public static ArrayList<IntegerPair> possiblepositions(int i, int j, int r, int c){// returns possible neighbours

        ArrayList<IntegerPair> neighbours = new ArrayList<IntegerPair>();
        for (int k = 0; k < 4; k++){
            if (inRange(0,r-1,i + movements[k][0]) && inRange(0,c-1,j + movements[k][1])){
                neighbours.add(new IntegerPair(i + movements[k][0], j + movements[k][1]));
            }
        }
        return neighbours;
    }  
    public static void main(String[] args) throws IOException {
        PrintWriter pw = new PrintWriter(System.out);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]), M = Integer.parseInt(firstLine[1]), Q = Integer.parseInt(firstLine[2]);
        String[] grid = new String[N];
        for (int i = 0; i < N; i++) grid[i] = br.readLine().strip();
        int[][] labels_0 = new int[N][M];
        // label components without breaking any walls
        int c = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (labels_0[i][j] == 0 && grid[i].charAt(j) != '#') {
                    c++;
                    Stack<IntegerPair> frontier = new Stack<>();
                    frontier.add(new IntegerPair(i, j));
                    labels_0[i][j] = c;
                    while (!frontier.isEmpty()) {
                        IntegerPair curr = frontier.pop();
                        int x = curr.first(), y = curr.second();
                        for (IntegerPair p: possiblepositions(x, y, N, M)) {
                            int a = p.first(), b = p.second();
                            if (grid[a].charAt(b) != '#' && labels_0[a][b] == 0) {
                                labels_0[a][b] = c;
                                frontier.push(p);
                            }
                        }
                    }
                }
            }
        }
        // there are c components
        ArrayList<HashSet<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < c + 1; i++) adjList.add(new HashSet<>());
        // an edge exists between component a and component b if it is possible to get from a to b by breaking one wall
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (labels_0[i][j] > 0) {
                    ArrayList<IntegerPair> neighbours = possiblepositions(i, j, N, M);
                    for (IntegerPair p: neighbours) {
                        int a = p.first(), b = p.second();
                        for (IntegerPair p2: possiblepositions(a, b, N, M)) {
                            int x = p2.first(), y = p2.second();
                            if (labels_0[i][j] != labels_0[x][y]) {
                                adjList.get(labels_0[i][j]).add(labels_0[x][y]);
                                adjList.get(labels_0[x][y]).add(labels_0[i][j]);
                            }
                        }
                    }
                }
            }
        }
        // resolve queries
        for (int i = 0; i < Q; i++) {
            String[] line = br.readLine().split(" ");
            int A = Integer.parseInt(line[0]) - 1, B = Integer.parseInt(line[1]) - 1, C = Integer.parseInt(line[2]) - 1, D = Integer.parseInt(line[3]) - 1, K = Integer.parseInt(line[4]);
            pw.println((labels_0[A][B] == labels_0[C][D] || (K == 1 && adjList.get(labels_0[A][B]).contains(labels_0[C][D]))) ? "yes" : "no");
        }
        br.close();
        pw.close();
    }
}
