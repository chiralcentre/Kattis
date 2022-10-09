import java.io.*;
import java.util.*;

public class distracted {
    public static String solve(int L, int N, HashSet<String> married, HashSet<String> unmarried, HashSet<String> unknown, BufferedReader br) throws IOException{
        if (L == 0) return "0";
        HashMap<String,String> adjList = new HashMap<>();
        for (int i = 0; i < L; i++) {
            String[] line = br.readLine().split(" -> ");
            String u = line[0], v = line[1];
            if (married.contains(u) && unmarried.contains(v)) {
                return "1";
            }
            if (married.contains(u) && unknown.contains(v) || 
                unknown.contains(u) && unknown.contains(v) || 
                unknown.contains(u) && unmarried.contains(v)) adjList.put(u,v);
        }
        if (adjList.size() > 0) {
            for (String u: adjList.keySet()) {
                if (married.contains(u)) {
                    String temp = u;
                    while (adjList.containsKey(temp)) {
                        temp = adjList.get(temp);
                        if (unmarried.contains(temp)) {
                            return "1";
                        }
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
        HashSet<String> married = new HashSet<>(), unmarried = new HashSet<>(), unknown = new HashSet<>();
        for (int i = 0; i < N; i++) {
            String[] line = br.readLine().split(" ");
            String name = line[0], status = line[1];
            if (status.equals("m")) married.add(name);
            else if (status.equals("u")) unmarried.add(name);
            else unknown.add(name);
        }
        pw.printf("%s\n",solve(L, N, married, unmarried, unknown, br));
        br.close();
        pw.close();
    }
}
