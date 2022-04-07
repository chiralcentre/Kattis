import java.io.*;
import java.util.ArrayList;
import java.util.Stack;

class Node implements Comparable<Node> {// stores coordinates
    private Integer f1, f2;
  
    public Node(Integer f, Integer s) {
        f1 = f;
        f2 = s;
    }
  
    public int compareTo(Node o) {
        if (!this.first().equals(o.first())) return this.first() - o.first();
        else return this.second() - o.second();
    }
  
    public Integer first() {return f1;}
  
    public Integer second() {return f2;}

    public void setFirst(int a) {f1 = a;}
    
    public void setSecond(int b) {f2 = b;}
}

public class hyacinth {
    public static int findLeaf(int[] degree){
        for (int i = 0; i < degree.length; i++){
            if (degree[i] == 1) return i;
        }
        return -1;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine()); int[] deg = new int[N]; //keeps track of degree of each node
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
        Node[] NIC = new Node[N];
        for (int i = 0; i < N; i++) { //initialisation
            adjList.add(new ArrayList<Integer>());
            NIC[i] = new Node(0, 0);
        } 
        for (int i = 0; i < N - 1; i++){
            String[] line = br.readLine().split(" ");
            int a = Integer.parseInt(line[0]) - 1, b = Integer.parseInt(line[1]) - 1; // offset by 1 due to zero indexing
            adjList.get(a).add(b); adjList.get(b).add(a);
            deg[a]++; deg[b]++; 
        }
        // findLeaf returns first index of leaf
        int leaf = findLeaf(deg), counter = 2;
        Stack<Integer> frontier = new Stack<>(); boolean[] visited = new boolean[N];
        frontier.push(leaf); visited[leaf] = true; 
        NIC[leaf].setFirst(1); NIC[leaf].setSecond(2); // initialise frequencies of starting node with 1 and 2
        while (!frontier.isEmpty()){ // carry out DFS from leaf
            int u = frontier.pop();
            for (int v: adjList.get(u)){ // v is a neighbour of u
                if (!visited[v]){
                    visited[v] = true;
                    if (deg[v] == 1){ // if node is a leaf, inherit frequencies from parent
                        NIC[v].setFirst(NIC[u].first());
                        NIC[v].setSecond(NIC[u].second());
                    }
                    else{
                        counter++;
                        NIC[v].setFirst(NIC[u].second()); // f2 > f1 
                        NIC[v].setSecond(counter); //increment counter and assign to NIC[v].f2
                        frontier.push(v);
                    }
                }
            }
        }
        for (int i = 0; i < N; i++) pw.printf("%d %d%n",NIC[i].first(),NIC[i].second());
        br.close();
        pw.close();
    }
}
