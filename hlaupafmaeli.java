import java.io.*;

public class hlaupafmaeli {
    public static long leap_year_count(long x) {
        return (x >> 2) - x / 100 + x / 400;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        long Y = Long.parseLong(br.readLine());
        if ((Y % 4 != 0) || ((Y % 100 == 0) && (Y % 400 != 0))) pw.println("Neibb");
        else pw.println(leap_year_count(Y) - leap_year_count(2020));
        br.close();
        pw.close();
    }
}
