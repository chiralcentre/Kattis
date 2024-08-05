import java.util.*;
import java.io.*;

public class storafmaeli {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = Integer.parseInt(br.readLine());
        pw.println(n % 10 == 0 ? "Jebb": "Neibb");
        br.close();
        pw.close();
    }
}