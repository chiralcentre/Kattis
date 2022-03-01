import java.io.*;
import java.util.*;

public class joinstrings {
    // Java's recursion depth limit is about 9000 
    public static void recursive_graph_traversal(ArrayList<ArrayDeque<Integer>> graph,String[] words, int lastIndex, PrintWriter pw){
        pw.print(words[lastIndex]);
        // while not empty, recursively traverse the graph
        while (graph.get(lastIndex).size() > 0) {
            int nextIndex = graph.get(lastIndex).removeFirst();
            recursive_graph_traversal(graph, words, nextIndex, pw);
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine()), lastIndex = 0;
        String[] words = new String[N];
        // an arraylist of deques is used to represent the relationship between the points
        // removal from the left is required in the graph traversal, so deques allow for O(1) removal from the left
        // graph[a] = [b] means that there is a directed edge from a to b
        // graph[a] = [b,c] and graph[b] = [d] means that there is a directed edge from a to b, then from b to d, and from d to c
        ArrayList<ArrayDeque<Integer>> graph = new ArrayList<ArrayDeque<Integer>>(); 
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine().strip();
            graph.add(new ArrayDeque<Integer>()); // empty deque is added to graph for initialisation
        }
        for (int i = 0; i < N-1; i++){
            String[] line = br.readLine().split(" ");
            // offset by one due to zero indexing
            int a = Integer.parseInt(line[0]) - 1, b = Integer.parseInt(line[1]) - 1;
            graph.get(a).addLast(b); // add a connection from a to b
            lastIndex = a; //lastIndex is the start point of the graph traversal
        }
        if (N == 1) {pw.println(words[0]);} // only one word
        else {recursive_graph_traversal(graph,words,lastIndex,pw);}
        br.close();
        pw.close();
    }
}
