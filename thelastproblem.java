import java.io.*;

public class thelastproblem {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String name = br.readLine().strip();
        pw.printf("Thank you, %s, and farewell!%n",name);
        br.close();
        pw.close();
    }
}
