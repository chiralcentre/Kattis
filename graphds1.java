import java.io.*;
import java.util.*;

public class graphds1 {
    public static ArrayList<ArrayList<Integer>> adjList;
    public static int[] colour;
    public static int isBipartite = 1;

    public static boolean isConnected(int N, int M) {
        if (M != N - 1) return false;
        // check if graph is connected
        Stack<Integer> frontier = new Stack<>();
        boolean[] visited = new boolean[N];
        frontier.push(0); visited[0] = true; int seen = 1;
        while (!frontier.isEmpty()) {
            int u = frontier.pop();
            for (int v: adjList.get(u)) {
                if (!visited[v]) {
                    visited[v] = true;
                    frontier.push(v);
                    seen++;
                }
            }
        }
        return seen == N;
    }

    // u is current vertex, c is colour to be assigned
    public static void DFS(int u, int c) {
        if (isBipartite == 0) return;
        if (colour[u] != 2) {
            // colour of node is different from colour to be assigned
            if (colour[u] != c) isBipartite = 0;
            return;
        } else { // not coloured yet
            colour[u] = c;
            for (int v: adjList.get(u)) {
                if (c == 1) DFS(v, 0);
                else DFS(v, 1);
            }
        }
    }

    public static ArrayList<Integer> kahn_toposort(int[] indeg, int N) {
        Queue<Integer> frontier = new ArrayDeque<Integer>();
        ArrayList<Integer> toposort = new ArrayList<Integer>();
        for (int i = 0; i < N; i++) {
            if (indeg[i] == 0) frontier.offer(i);
        }
        while (!frontier.isEmpty()) {
            int u = frontier.poll();
            toposort.add(u);
            for (int v: adjList.get(u)) { 
                indeg[v]--;
                if (indeg[v] == 0) frontier.offer(v);
            }
        }
        return toposort;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out); 
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]), M = Integer.parseInt(firstLine[1]), T = Integer.parseInt(firstLine[2]);
        int[] indeg = new int[N], outdeg = new int[N];
        adjList = new ArrayList<ArrayList<Integer>>();
        Stack<Integer> frontier = new Stack<>();
        boolean[] visited = new boolean[N];
        for (int i = 0; i < N; i++) adjList.add(new ArrayList<Integer>());
        for (int i = 0; i < M; i++) {
            String[] line = br.readLine().split(" ");
            int u = Integer.parseInt(line[0]), v = Integer.parseInt(line[1]);
            adjList.get(u).add(v);
            indeg[v]++;
            outdeg[u]++;
            if (T == 1) adjList.get(v).add(u);
        }
        for (int i = 0; i < N; i++) {
            if (indeg[i] == 0) {
                frontier.push(i);
                visited[i] = true;
            }
        }
        int[] ans = new int[4];
        ans[0] = ((T == 1) && isConnected(N, M) && M == N - 1) ? 1 : 0;
        long n = (long) N, m = (long) M;
        ans[1] = ((T == 1 && n * (n - 1) == (m << 1)) || (T == 2 && n * (n - 1) == m)) ? 1 : 0;
        // check for bipartite graph in undirected graph
        if  (T == 1) {
            colour = new int[N];
            for (int i = 0; i < N; i++) colour[i] = 2; // colour 2 means not visited
            for (int i = 0; i < N; i++) {
                if (isBipartite == 1 && colour[i] == 2) DFS(i,0);
            }
            ans[2] = isBipartite;
        } else { // check for bipartite graph in directed graph
            ans[2] = 1;
            for (int i = 0; i < N; i++) {
                if (indeg[i] >= 1 && outdeg[i] >= 1) {
                    ans[2] = 0;
                    break;
                }
            }
        }
        // if graph is undirected, it is definitely not a DAG
        if (T == 1) {
            ans[3] = (M > 0) ? 0: 1; // exception: no edges in an undirected graph is a DAG by default
        } else ans[3] = (kahn_toposort(indeg, N).size() == N) ? 1 : 0;
        // update tree status if graph is DAG
        if (ans[3] == 1 && M == N - 1 && frontier.size() == 1) {
            int seen = frontier.size();
            while (!frontier.isEmpty()) {
                int u = frontier.pop();
                for (int v: adjList.get(u)) {
                    if (!visited[v]) {
                        visited[v] = true;
                        frontier.push(v);
                        seen++;
                    }
                }
            }
            if (seen == N) ans[0] = 1;
        }
        pw.printf("%d %d %d %d\n",ans[0],ans[1],ans[2],ans[3]);
        br.close();
        pw.close();
    }
}
