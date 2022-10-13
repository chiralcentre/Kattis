import java.io.*;
import java.util.*;

class Fraction {
    private final int num;
    private final int denom;
  
    public Fraction(int num, int denom) {
        this.num = num;
        this.denom = denom;
    }

    public int getNum() {
        return this.num;
    }

    public int getDenom() {
        return this.denom;
    }

    @Override
    public boolean equals(Object obj) { 
        if (obj == this) return true;
        if (obj instanceof Fraction) {
            Fraction f = (Fraction) obj;
            return f.num == this.num && f.denom == this.denom;
        }
        else return false;
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.num,this.denom);
    }
}

public class maxcolinear {
    // Returns greatest common divisor of a and b
    public static int gcd(int a, int b) {
        int rem = 0;
        while (b > 0) { 
            rem = a % b;
            a = b;
            b = rem;
        }
        return a;  
    }

    public static Fraction gradient(int x1, int y1, int x2, int y2) {
        if (x2 == x1) {//undefined gradient
            return new Fraction(1, 0); //standardise undefined gradient tuple as (1,0)
        }
        int rise = y2 - y1, run = x2 - x1;
        if (run < 0) {
            rise = -rise; run = -run; //standardise so that denominator will never be negative
        }
        int d = gcd(Math.abs(rise),run); //calculate gcd taking positive values
        return new Fraction(rise / d, run / d);
    }

    public static int maxCollinearPoints(int[] xcoords, int[] ycoords, int n) {
        // at least three points are needed for points to be possibly non collinear
        if (n < 3) return n;
        int highest = 0;
        for (int i = 0; i < n - 1; i++) {
            HashMap<Fraction,Integer> slopes = new HashMap<>();
            for (int j = i + 1; j < n; j++) {
                Fraction grad = gradient(xcoords[i], ycoords[i], xcoords[j], ycoords[j]);
                Integer prev = slopes.get(grad);
                if (prev == null) slopes.put(grad,2); //every two points form a line
                else slopes.put(grad, prev + 1);
                Integer updated = slopes.get(grad);
                if (updated > highest) highest = updated;
            }
        }
        return highest;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            int[] xcoords = new int[n], ycoords = new int[n];
            for (int i = 0; i < n; i++) {
                String[] line = br.readLine().split(" ");
                xcoords[i] = Integer.parseInt(line[0]); ycoords[i] = Integer.parseInt(line[1]);
            }
            pw.printf("%d\n", maxCollinearPoints(xcoords,ycoords,n));
        }
        br.close();
        pw.close();
    }
}
