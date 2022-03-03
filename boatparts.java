import java.io.*;
import java.util.*;

public class boatparts {
    public static int theseus(int P, int N, BufferedReader br) throws IOException{
        Set<String> parts = new HashSet<>();
        for (int i = 1; i <= N; i++){
            String part = br.readLine().strip();
            if (!parts.contains(part)) {parts.add(part);}
            if (parts.size() == P) {return i;}
        }
        return -1; // paradox avoided
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int P = Integer.parseInt(firstLine[0]), N = Integer.parseInt(firstLine[1]);
        int result = theseus(P, N, br); 
        pw.println(result != - 1 ? result : "paradox avoided");
        br.close();
        pw.close();
    }
}
