import java.io.*;
import java.util.*;

public class dominos {
    public static void DFSrec(int key, boolean[] visited, ArrayList<ArrayList<Integer>> adjacencyList, ArrayList<Integer> reversedToposort){
        visited[key] = true;
        for (int v: adjacencyList.get(key)){
            if (!visited[v]) {DFSrec(v,visited,adjacencyList,reversedToposort);}
        }
        reversedToposort.add(key);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++){
            String[] line = br.readLine().split(" ");
            int n = Integer.parseInt(line[0]), m = Integer.parseInt(line[1]), counter = 0; //counter keeps track of minimum number of dominos to topple
            ArrayList<ArrayList<Integer>> adjacencyList = new ArrayList<>();
            for (int j = 0; j < n; j++) {adjacencyList.add(new ArrayList<Integer>());} //initialisation with n arraylists
            for (int j = 0; j < m; j++) {
                String[] relation = br.readLine().split(" ");
                int a = Integer.parseInt(relation[0]) - 1, b = Integer.parseInt(relation[1]) - 1; // offset by 1 due to zero indexing
                adjacencyList.get(a).add(b);
            }
            // Perform DFS topological sort (postorder DFS) instead of Kahn's algorithm as graph may have cycles
            boolean[] visited = new boolean[n]; //boolean array automatically initialised to false
            ArrayList<Integer> reversedToposort = new ArrayList<>();
            for (int k = 0; k < n; k++) {
                if (!visited[k]) {DFSrec(k,visited,adjacencyList,reversedToposort);}
            }
            // iterate through reversedToposort from right to left, since it is in reverse order
            // For each vertex in reversedToposort, if it is not visited already, add 1 to the answer, and perform DFS from
            // that vertex, marking any vertices found during the traversal as visited
            visited = new boolean[n]; //reset visited array
            for (int j = reversedToposort.size()-1; j >= 0; j--){
                // iterative version of DFS is used here
                if (!visited[reversedToposort.get(j)]){
                    counter += 1;
                    Stack <Integer> s = new Stack<>(); s.push(reversedToposort.get(j));
                    while (s.size() > 0) {
                        int u = s.pop();
                        for (int v: adjacencyList.get(u)){
                            if (!visited[v]){
                                s.push(v);
                                visited[v] = true;
                            }
                        }
                    }
                }
            }
            pw.println(counter);
        }
        
        br.close();
        pw.close();
    }
}
