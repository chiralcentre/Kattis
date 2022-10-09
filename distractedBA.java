import java.io.*;
import java.util.*;

public class distracted {
    public static String solve(int L, int N, HashSet<Integer> married, HashSet<Integer> unmarried, HashSet<Integer> unknown, HashMap<String,Integer> nameToIndex, BufferedReader br) throws IOException{
        if (L == 0) return "0";
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < N; i++) adjList.add(new ArrayList<Integer>());
        boolean additions = false;
        for (int i = 0; i < L; i++) {
            String[] line = br.readLine().split(" -> ");
            String f = line[0], s = line[1];
            int u = nameToIndex.get(f), v = nameToIndex.get(s);
            if (married.contains(u) && unmarried.contains(v)) {
                return "1";
            }
            if (married.contains(u) && unknown.contains(v) || 
                unknown.contains(u) && unknown.contains(v) || 
                unknown.contains(u) && unmarried.contains(v)) {
                    adjList.get(u).add(v);
                    additions = true;
            }
        }
        if (additions) {
            Stack<Integer> frontier = new Stack<>();
            boolean[] visited = new boolean[N];
            for (int u: married) {
                if (adjList.get(u).size() > 0) {
                    frontier.push(u);
                    visited[u] = true;
                }
            }
            while (!frontier.empty()) {
                int u = frontier.pop();
                for (int v: adjList.get(u)) {
                    if (!visited[v]){
                        if (unmarried.contains(v)) return "1";
                        frontier.push(v);
                        visited[v] = true;
                    }
                }
            }
            return "?";
        }
        return "0";
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]), L = Integer.parseInt(firstLine[1]);
        HashSet<Integer> married = new HashSet<>(), unmarried = new HashSet<>(), unknown = new HashSet<>();
        HashMap<String,Integer> nameToIndex = new HashMap<>();
        for (int i = 0; i < N; i++) {
            String[] line = br.readLine().split(" ");
            String name = line[0], status = line[1];
            nameToIndex.put(name,i);
            if (status.equals("m")) married.add(i);
            else if (status.equals("u")) unmarried.add(i);
            else unknown.add(i);
        }
        pw.printf("%s\n",solve(L, N, married, unmarried, unknown, nameToIndex, br));
        br.close();
        pw.close();
    }
}
