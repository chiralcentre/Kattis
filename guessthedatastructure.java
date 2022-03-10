import java.io.*;
import java.util.*;

public class guessthedatastructure {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String str = " ";
        while ((str = br.readLine()) != null){// check for EOF
            int n = Integer.parseInt(str);
            Stack<Integer> S = new Stack<>();
            Queue<Integer> Q = new LinkedList<>();
            PriorityQueue<Integer> PQ = new PriorityQueue<>(Collections.reverseOrder());
            HashSet<String> dataStructures = new HashSet<>();
            dataStructures.add("Stack"); dataStructures.add("Queue"); dataStructures.add("Priority Queue");
            boolean impossible = false;
            for (int i = 0; i < n; i++){
                String[] line = br.readLine().split(" ");
                int command = Integer.parseInt(line[0]), element = Integer.parseInt(line[1]);
                if (command == 1){
                    S.push(element);
                    Q.offer(element);
                    PQ.add(element);
                }
                else {
                    if (S.size() == 0 || Q.size() == 0 || PQ.size() == 0){impossible = true;}
                    else {
                        int a = S.pop(), b = Q.poll(), c = PQ.remove();
                        if (a != element) {dataStructures.remove("Stack");}
                        if (b != element) {dataStructures.remove("Queue");}
                        if (c != element) {dataStructures.remove("Priority Queue");}
                    }
                }
            }
            if (impossible || dataStructures.size() == 0) {pw.println("impossible");}
            else if (dataStructures.size() == 1) {pw.println(dataStructures.toArray()[0]);}
            else if (dataStructures.size() > 1) {pw.println("not sure");}
        }
        br.close();
        pw.close();
    }
}
