import java.io.*;

public class codetosavelives {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++){
            String[] firstLine = br.readLine().split(" "), secondLine = br.readLine().split(" ");
            int num1 = Integer.parseInt(String.join("", firstLine)), num2 = Integer.parseInt(String.join("", secondLine));
            String[] sum = Integer.toString(num1 + num2).split("");
            pw.println(String.join(" ",sum));
        }
        br.close();
        pw.close();
    }
}
