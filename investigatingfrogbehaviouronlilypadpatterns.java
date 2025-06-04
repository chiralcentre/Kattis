import java.io.*;
import java.util.*;

class Interval implements Comparable<Interval> {
    private final long start;
    private final long end;

    public Interval(long s, long e){
        this.start = s;
        this.end = e;
    }

    public long getStart() {return this.start;}

    public long getEnd() {return this.end;}

    @Override
    public int compareTo(Interval i) { // sort in ascending order of start time
        if (this.start != i.start) return Long.compare(this.start, i.start);
        return Long.compare(this.end, i.end);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) return true;
        else if (obj instanceof Interval) {
            Interval p = (Interval) obj;
            return p.start == this.start && p.end == this.end;
        } else return false;
    }

    @Override
    public String toString() {
        return String.format("[%d,%d]",this.start,this.end);
    }
}

public class investigatingfrogbehaviouronlilypadpatterns {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine());
        String[] firstLine =  br.readLine().split(" ");
        long[] mappings =  new long[N + 1];
        TreeSet<Interval> intervals = new TreeSet<>();
        for (int i = 0; i < N; i++) mappings[i] = Long.parseLong(firstLine[i]);
        long s = mappings[0], e = mappings[0];
        for (int i = 1; i < N; i++) {
            if (mappings[i] - mappings[i - 1] != 1) {
                intervals.add(new Interval(s, e));
                s = mappings[i]; 
            }
            e = mappings[i];
        }
        intervals.add(new Interval(s, e));
        int Q = Integer.parseInt(br.readLine());
        for (int i = 0; i  < Q; i++) {
            int p = Integer.parseInt(br.readLine()) - 1; // offset by 1 due to zero indexing
            long c = mappings[p];
            // there is exactly one interval containing c, denoted as a
            // let a = [s, e]
            // if c != s, new intervals = [s, c - 1], [c + 1, e + 1] 
            // if c == s, new intervals = [c + 1, e + 1]
            // interval [c + 1, e + 1] may have to be merged with higher intervals
            Interval v = new Interval(c, (long) 1e7), a = intervals.lower(v);
            s = a.getStart(); e = a.getEnd();
            pw.printf("%d\n", e + 1);
            mappings[p] = e + 1;
            intervals.remove(a);
            if (c != s) intervals.add(new Interval(s, c - 1));
            v = new Interval(c + 1, e + 1); 
            Interval b = intervals.higher(v);
            // merge with intervals above, this occurs at most once
            if (b != null && b.getStart() == v.getEnd() + 1) {
                intervals.remove(b);
                v = new Interval(c + 1, b.getEnd());
            }
            intervals.add(v);
            // for (Interval j: intervals) pw.printf("%s, ", j);
            // pw.printf("\n");
        }
        br.close();
        pw.close();
    }
}