import java.io.*;
import java.math.BigInteger;

public class lidaskipting2 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        BigInteger n = new BigInteger(br.readLine());
        BigInteger[] x = n.divideAndRemainder(new BigInteger("3"));
        if (!x[1].equals(BigInteger.ZERO)) x[0] = x[0].add(new BigInteger("1"));
        pw.println(n);
        pw.println(x[0]);
        br.close();
        pw.close();
    }
}
