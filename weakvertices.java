import java.io.*;
import java.util.*;

public class weakvertices {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == -1) {break;}
            ArrayList<HashSet<Integer>> adjacencySets = new ArrayList<HashSet<Integer>>(); 
            ArrayList<String> weakVertices = new ArrayList<String>();
            for (int i = 0; i < n; i++){adjacencySets.add(new HashSet<Integer>());} //initialisation
            for (int i = 0; i < n; i++){
                String[] line = br.readLine().split(" ");
                // due to symmetric nature of adjacency matrix, only need to consider entries below or above diagonal
                // in this case we take bottom half
                for (int j = 0; j < i; j++) {
                    if (Integer.parseInt(line[j]) == 1){
                        adjacencySets.get(i).add(j);
                        adjacencySets.get(j).add(i);
                    }
                }
            }
            for (int k = 0; k < n; k++){
                boolean weak = true;
                for (int neighbour: adjacencySets.get(k)){
                    HashSet<Integer> otherNeighbours = new HashSet<>();
                    for (int x: adjacencySets.get(k)) {
                        if (x != neighbour) {otherNeighbours.add(x);} //create a set of neighbours of k without neighbour in it
                    }
                    // check if k has at least two different neighbours that are direct neighbours of each other
                    otherNeighbours.retainAll(adjacencySets.get(neighbour));
                    if (otherNeighbours.size() > 0){
                        weak = false;
                        break;
                    }
                }
                if (weak) {weakVertices.add(Integer.toString(k));}
            }
            pw.println(String.join(" ",weakVertices));
        }
        br.close();
        pw.close();
    }
}
