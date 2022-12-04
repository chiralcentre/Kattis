import java.util.*;
import java.io.*;

public class reactivity {
    public static boolean isUniqueToposort(ArrayList<Integer> toposort, ArrayList<HashSet<Integer>> adjList) {
        for (int i = 0; i < toposort.size() - 1; i++) {
            if (!adjList.get(toposort.get(i)).contains(toposort.get(i + 1))) return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]), K = Integer.parseInt(firstLine[1]);
        ArrayList<HashSet<Integer>> adjList = new ArrayList<HashSet<Integer>>();
        for (int i = 0; i < N; i++) adjList.add(new HashSet<Integer>());
        int[] indeg = new int[N];
        for (int i = 0; i < K; i++) {
            String[] line = br.readLine().split(" ");
            int u = Integer.parseInt(line[0]), v = Integer.parseInt(line[1]);
            adjList.get(u).add(v);
            indeg[v]++;
        }
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
        if (isUniqueToposort(toposort, adjList)) {
            for (int i = 0; i < toposort.size(); i++) {
                pw.print(toposort.get(i));
                if (i < toposort.size() - 1) pw.print(" ");
            }
            pw.print("\n");
        } else {
            pw.println("back to the lab");
        }
        
        br.close();
        pw.close();
    }
}
