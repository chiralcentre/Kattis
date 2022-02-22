import java.io.*;
import java.util.BitSet;

class Sieve{
    private BitSet sieve;
    private int primes;

    public Sieve(BitSet sieve, int primes){
        this.sieve = sieve;
        this.primes = primes;
    }

    public BitSet getSieve() {return this.sieve;}

    public int getNumOfPrimes() {return this.primes;}
}
public class primesieve {
    public static Sieve SieveOfEratosthenes(int n){
        BitSet sieve = new BitSet(n+1); //bitset is used to reduce memory usage
        for (int i = 0; i <= n; i++) sieve.set(i);
        int p = 2, counter = n+1; //counter stores number of primes
        while (p*p <= n){
            if (sieve.get(p) == true){
                for (int j = 2*p; j <= n; j += p){
                    if (sieve.get(j) == true) counter -= 1;
                    sieve.set(j,false);
                }
            }
            p += 1;
        }
        // 0 and 1 are not prime numbers
        sieve.set(0, false); sieve.set(1, false); counter -= 2;
        return new Sieve(sieve,counter);
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]), t = Integer.parseInt(firstLine[1]);
        Sieve result = SieveOfEratosthenes(n);
        pw.println(result.getNumOfPrimes());
        for (int i = 0; i < t; i++){
            pw.println(result.getSieve().get(Integer.parseInt(br.readLine())) == true ? '1' : '0');
        }
        br.close();
        pw.close();
    }
}
