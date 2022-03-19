import java.io.*;

public class herman {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        double R = Double.parseDouble(br.readLine());
        pw.println(Math.PI*R*R);
        pw.println(2*R*R);
        br.close();
        pw.close();
    }
}
