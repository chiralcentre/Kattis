import java.io.*;

public class symmetricorder {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int counter = 1;
        while (true){
            int n = Integer.parseInt(br.readLine());
            int start = 0, end = n - 1;
            if (n == 0) break;
            String[] names = new String[n];
            while (start < end) {
                names[start] = br.readLine().strip();
                names[end] = br.readLine().strip();
                start += 1; end -= 1;
            }
            if (start == end) names[start] = br.readLine().strip();
            pw.printf("SET %d%n",counter);
            for (String s: names) pw.println(s);
            counter += 1;
        }
        br.close();
        pw.close();
    }
}
