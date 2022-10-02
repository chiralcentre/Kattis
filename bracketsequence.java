import java.io.*;
import java.util.Stack;

public class bracketsequence {
    public static long MODULO = 1000000007L;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out))); 
        br.readLine(); //value of N not needed
        String[] tokens = br.readLine().split(" ");
        boolean alt = true;
        Stack<Object> stack = new Stack<>();
        for (String t: tokens) {
            if (t.equals(")")) {
                long temp = alt ? 0 : 1;
                if (alt) {
                    while (!stack.isEmpty() && !stack.peek().equals("(")) {
                        temp += (Long) stack.pop();
                        temp %= MODULO;
                    }
                } else {
                    while (!stack.isEmpty() && !stack.peek().equals("(")) {
                        temp *= (Long) stack.pop();
                        temp %= MODULO;
                    }
                }
                stack.pop(); // remove left bracket
                stack.push(temp);
                alt = !alt;
            } else {
                if (t.equals("(")) {
                    alt = !alt;
                    stack.push(t);
                } else stack.push(Long.parseLong(t));
            }
        }
        long total = 0;
        while (!stack.isEmpty()) {
            total += (Long) stack.pop();
            total %= MODULO;
        }
        pw.printf("%d\n",total);
        br.close();
        pw.close();
    }
}
