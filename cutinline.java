import java.util.*;
import java.io.*;

public class cutinline {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        ArrayList<String> queue = new ArrayList<String>();
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) queue.add(br.readLine().strip());
        int Q = Integer.parseInt(br.readLine());
        for (int i = 0; i < Q; i++) {
            String[] line = br.readLine().split(" ");
            if (line[0].equals("cut")) queue.add(queue.indexOf(line[2]),line[1]);
            else queue.remove(line[1]);
        }
        for (String s: queue) pw.println(s);
        br.close();
        pw.close();
    }
}