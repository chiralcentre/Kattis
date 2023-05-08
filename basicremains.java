import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class basicremains {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] line = br.readLine().split(" ");
        while (!line[0].equals("0")) {
            int b = Integer.parseInt(line[0]);
            BigInteger p = new BigInteger(line[1], b);
            BigInteger m = new BigInteger(line[2], b);
            pw.println(p.mod(m).toString(b));
            line = br.readLine().split(" ");
        }
        br.close();
        pw.close();
    }
}