import java.io.*;
import java.util.*;

public class delimitersoup {
    // openingClosing stores opening parenthesis as key and closing parenthesis as value
    // closingOpening stores closing parenthesis as key and opening parenthesis as value
    public static final HashMap<Character,Character> openingClosing = new HashMap<>(){{ put('(', ')'); put('[', ']'); put('{', '}'); }};
    public static final HashMap<Character,Character> closingOpening = new HashMap<>(){{ put(')', '('); put(']', '['); put('}', '{'); }};

    public static String delimitercheck(String delimiters, int strlen){
        Stack<Character> parentheses = new Stack<Character>();
        for (int i = 0; i < strlen; i++){
            if (openingClosing.containsKey(delimiters.charAt(i))) {parentheses.add(delimiters.charAt(i));}
            else if (closingOpening.containsKey(delimiters.charAt(i))){
                if (parentheses.empty() || parentheses.pop() != (closingOpening.get(delimiters.charAt(i)))){
                    return String.format("%s %d", delimiters.charAt(i), i);
                }
            }
        }
        return "ok so far"; // if no errors are found
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine().strip();
        pw.println(delimitercheck(s,n));
        br.close();
        pw.close();
    }
}
