import java.io.*;
import java.util.*;

public class managingpackaging {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        boolean first = true;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            if (first) first = false;
            else pw.print("\n");
            HashMap<String,Integer> filesToIndex = new HashMap<>();
            HashMap<Integer,String> indexToFiles = new HashMap<>();
            int counter = 0;
            ArrayList<ArrayList<Integer>> adjList = new ArrayList<ArrayList<Integer>>();
            int[] indeg = new int[n];
            for (int i = 0; i < n; i++) adjList.add(new ArrayList<Integer>());
            for (int i = 0; i < n; i++) {
                String[] line = br.readLine().split(" ");
                String f = line[0];
                Integer idx = filesToIndex.get(f);
                if (idx == null) {
                    idx = counter;
                    filesToIndex.put(f,counter);
                    indexToFiles.put(counter,f);
                    counter++;
                }
                for (int j = 1; j <  line.length; j++) {
                    String dep = line[j];
                    Integer depIdx = filesToIndex.get(dep);
                    if (depIdx == null) {
                        depIdx = counter;
                        filesToIndex.put(dep,counter);
                        indexToFiles.put(counter,dep);
                        counter++;
                    }
                    // a directed edge from dependencies to file exists
                    adjList.get(depIdx).add(idx); 
                    indeg[idx]++;
                }
            } 
            //Create a min heap and insert all vertices with indegree 0 in O(n) time
            //A min heap is used to ensure the lexicographically smallest vertex is picked every time
            //modified Kahn's algorithm with time complexity of O(n log n + E) where E is number of edges
            PriorityQueue<String> pq = new PriorityQueue<>();
            for (int i = 0; i < n; i++) {
                if (indeg[i] == 0) pq.add(indexToFiles.get(i));
            }
            ArrayList<String> toposort = new ArrayList<>();
            int V = 0;
            while (!pq.isEmpty()) {
                String u = pq.poll();
                toposort.add(u);
                for (int v: adjList.get(filesToIndex.get(u))) {
                    indeg[v]--;
                    if (indeg[v] == 0) {
                        pq.add(indexToFiles.get(v));
                    }
                }
                V++;
            }
            // cycle exists if V != n
            if (V != n) pw.print("cannot be ordered\n");
            else {
                for (String file: toposort) pw.printf("%s\n",file);
                pw.print("\n");
            }
        }
        br.close();
        pw.close();
    }
}
