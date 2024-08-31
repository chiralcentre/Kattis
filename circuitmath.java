import java.io.*;
import java.util.Stack;

public class circuitmath {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = Integer.parseInt(br.readLine());
        String[] firstLine = br.readLine().split(" ");
        boolean[] truthValues = new boolean[n];
        for (int i = 0; i < n; i++) truthValues[i] = firstLine[i].equals("T");
        String[] circuit = br.readLine().split(" ");
        Stack<Boolean> stack = new Stack<>();
        for (String part: circuit) {
            if (part.equals("*")) {
                boolean first = stack.pop(), second = stack.pop();
                stack.push(first && second);
            } else if (part.equals("+")) {
                boolean first = stack.pop(), second = stack.pop();
                stack.push(first || second);
            } else if (part.equals("-")) {
                boolean first = stack.pop();
                stack.push(!first);
            } else {
                stack.push(truthValues[part.charAt(0) - 65]);
            }
        }
        boolean ans = stack.peek();
        pw.println(ans ? "T" : "F");
        br.close();
        pw.close();
    }
}
