import java.io.*;
import java.util.*;

public class delimitersoup {
    public static String delimitercheck(String delimiters, int strlen){
        ArrayList<Character> parentheses = new ArrayList<Character>(); // parentheses arraylist will operate like a stack
        // openingClosing stores opening parenthesis as key and closing parenthesis as value
        // closingOpening stores closing parenthesis as key and opening parenthesis as value
        HashMap<Character,Character> openingClosing = new HashMap<>(), closingOpening = new HashMap<>();
        openingClosing.put('(',')'); openingClosing.put('[',']'); openingClosing.put('{','}');
        closingOpening.put(')','('); closingOpening.put(']','['); closingOpening.put('}','{');
        for (int i = 0; i < strlen; i++){
            if (openingClosing.containsKey(delimiters.charAt(i))) {parentheses.add(delimiters.charAt(i));}
            else if (closingOpening.containsKey(delimiters.charAt(i))){
                if (parentheses.size() == 0 || parentheses.remove(parentheses.size()-1) != (closingOpening.get(delimiters.charAt(i)))){
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
