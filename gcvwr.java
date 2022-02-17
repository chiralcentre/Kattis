import java.io.*;

public class gcvwr {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" "), secondLine = br.readLine().split(" ");
        int G = Integer.parseInt(firstLine[0]), T = Integer.parseInt(firstLine[1]), N = Integer.parseInt(firstLine[2]), sum = 0;
        for (int i = 0; i < N; i++) {sum += Integer.parseInt(secondLine[i]);}
        pw.println((int) Math.floor((G-T)*0.9-sum));
        br.close();
        pw.close();
    }
}
