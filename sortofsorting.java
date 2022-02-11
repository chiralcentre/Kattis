import java.io.*;
import java.util.*;

class NameComparator implements Comparator<String>{
    public int compare(String s1, String s2){
        int a = Character.compare(s1.charAt(0),s2.charAt(0));
        return a != 0 ? a: Character.compare(s1.charAt(1),s2.charAt(1)); // sort by first letter, followed by second letter
    }
    public boolean equals(Object obj){return this == obj;}
}

public class sortofsorting {
    public static void main(String[] args) throws IOException{
        NameComparator nComp = new NameComparator();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        boolean first = true;
        while (true){
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            if (first){first = false;}
            else {pw.println();} // new line between test cases
            ArrayList<String> names = new ArrayList<>();
            for (int i = 0; i < n; i++) names.add(br.readLine().strip());
            Collections.sort(names,nComp);
            for (String s: names) pw.println(s);
        }
        br.close();
        pw.close();
    }
}
