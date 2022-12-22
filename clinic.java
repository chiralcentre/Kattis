import java.util.*;
import java.io.*;

class Patient implements Comparable<Patient> {
    long T,S,K;
    String M;

    Patient(long T, String M, long S, long K) {
        this.T = T;
        this.M = M;
        this.S = S;
        this.K = K;
    }

    @Override
    public int compareTo(Patient p) {
        long d = this.S - p.S + this.K * (p.T - this.T);
        if (d != 0) return d > 0 ? 1 : -1;
        return p.M.compareTo(this.M);
    }

    @Override
    public String toString() {
        return this.M;
    }
}

//TreeSet solution TLEd
public class clinic {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        long K = Long.parseLong(firstLine[1]);
        PriorityQueue<Patient> pq = new PriorityQueue<>(Collections.reverseOrder());
        HashSet<String> deleted = new HashSet<>();
        for (int i = 0; i < N; i++) {
            String[] line = br.readLine().split(" ");
            int Q = Integer.parseInt(line[0]);
            if (Q == 1) {
                long T = Long.parseLong(line[1]), S = Long.parseLong(line[3]);
                String M = line[2]; Patient p = new Patient(T,M,S,K);
                pq.add(p);
            }
            else if (Q == 2) {
                while (!pq.isEmpty() && deleted.contains(pq.peek().M)) pq.poll();
                Patient p = pq.poll();
                pw.println(p == null ? "doctor takes a break" : p);
            } else {
                deleted.add(line[2]);
            }
        }
        br.close();
        pw.close();
    }
}
