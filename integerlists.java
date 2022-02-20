import java.io.*;
import java.util.*;

public class integerlists {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++){
            String program = br.readLine().strip();
            int n = Integer.parseInt(br.readLine());
            String[] line = br.readLine().split(",");
            if (n >= 2){
                line[0] = line[0].substring(1); //get rid of '['
                line[line.length-1] = line[line.length-1].substring(0, line[line.length-1].length()-1); //get rid of ']'
            }
            else if (n == 1) {line[0] = line[0].substring(1,line[0].length()-1);} //get rid of brackets
            ArrayDeque<String> lst = new ArrayDeque<>(Arrays.asList(line));
            boolean error = false, reverse = false;
            for (int j = 0; j < program.length(); j++){
                if (program.charAt(j) == 'R') {reverse = (reverse) ? false : true;}
                else { // drop command
                    if (n > 0){
                       if (reverse) lst.removeLast();
                       else lst.removeFirst();
                       n -= 1;
                    }
                    else{//empty list
                        error = true;
                        break;
                    }
                }
            }
            if (error){pw.println("error");}
            else{
                pw.print("[");
                if (n > 0){
                    if (reverse){
                        Iterator<String> iter = lst.descendingIterator();
                        while (iter.hasNext()){
                            pw.print(iter.next());
                            if (iter.hasNext()) pw.print(",");
                        }
                    }
                    else{
                        Iterator<String> iter = lst.iterator();
                        while (iter.hasNext()){
                            pw.print(iter.next());
                            if (iter.hasNext()) pw.print(",");
                        }
                    }
                }
                pw.print("]\n");
            }
        }
        br.close();
        pw.close();
    }
}

