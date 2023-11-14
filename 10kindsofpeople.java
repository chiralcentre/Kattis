import java.io.*;
import java.util.*;

class tenkindsofpeople {
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
        PrintWriter out = new PrintWriter(System.out);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] l = br.readLine().split(" ");
        int l1 = Integer.parseInt(l[0]);
        int l2 = Integer.parseInt(l[1]);
        String[] graph = new String[l1];
        int[][] label = new int[l1][l2];

        int count = 0;

        for (int i = 0; i < l1; i++) graph[i] = br.readLine().strip();

        //Traversing the graph
        for (int i = 0; i < l1; i++) {
            for (int j = 0; j < l2; j++) {
                //If not labeled.
                if (label[i][j] == 0) {
                    count++;
                    Stack<IntegerPair> frontier = new Stack<>();
                    char start = graph[i].charAt(j);
                    frontier.add(new IntegerPair(i, j));
                    while (!frontier.isEmpty()) {
                        IntegerPair curr = frontier.pop();
                        int x = curr.first(), y = curr.second();
                        // Labelling every visited vertex.
                        label[x][y] = count;
                        for (IntegerPair p: possiblepositions(x, y, l1, l2)) {
                            int a = p.first(), b = p.second();
                            if (label[a][b] == 0 && graph[a].charAt(b) == start) {
                                label[a][b] = count;
                                frontier.push(p);
                            }
                        }

                    }
                }
            }
        }

        int q = Integer.parseInt(br.readLine());
        for (int i = 0; i < q; i++) {
            String[] o = br.readLine().split(" ");
            int s1 = Integer.parseInt(o[0]) - 1;
            int s2 = Integer.parseInt(o[1]) - 1;
            int e1 = Integer.parseInt(o[2]) - 1;
            int e2 = Integer.parseInt(o[3]) - 1;
            if (label[s1][s2] == label[e1][e2]) {
                if (graph[s1].charAt(s2) == '0') {
                    out.println("binary");
                } else {
                    out.println("decimal");
                }
            } else {
                out.println("neither");
            }

        }
        out.flush();
    }
}



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


 
