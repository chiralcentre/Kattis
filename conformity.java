import java.io.*;
import java.util.*;

public class conformity {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = Integer.parseInt(br.readLine()), maximum = 0, counter = 0;
        HashMap <Set<String>,Integer> courses = new HashMap<>();
        for (int i = 0; i < n; i++){
            String[] line = br.readLine().split(" ");
            Set<String> combination = new HashSet<>(Arrays.asList(line));
            if (courses.containsKey(combination)){courses.put(combination,courses.get(combination)+1);}
            else {courses.put(combination,1);}
        }
        // iterate through values to find highest popularity count
        for (Integer value: courses.values()){if (value > maximum){maximum = value;}}
        // iterate over key value pairs and increment counter accordingly
        for (Map.Entry<Set<String>, Integer> combination: courses.entrySet()){
            if (combination.getValue() == maximum) {counter += combination.getValue();}
        }
        pw.println(counter);
        br.close();
        pw.close();
    }
}
