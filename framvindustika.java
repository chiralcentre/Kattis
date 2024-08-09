import java.io.*;

public class framvindustika {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int p = Integer.parseInt(firstLine[0]), w = Integer.parseInt(firstLine[1]);
        int n = (p * w) / 100;
        pw.print("[");
        for (int i = 0; i < n; i++) pw.print("#");
        for (int i = 0; i < w - n; i++) pw.print("-");
        pw.print("] |");
        int L = String.valueOf(p).length();
        for (int i = 0; i < 4 - L; i++) pw.print(" ");
        pw.printf("%d",p);
        pw.println("%");
        br.close();
        pw.close();
    }
}
