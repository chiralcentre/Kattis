import java.io.*;
import java.util.*;

class Interval implements Comparable<Interval> {
    private long start, end;

    public Interval(long s, long e){
        this.start = s;
        this.end = e;
    }

    public long getStart() {return this.start;}

    public long getEnd() {return this.end;}

    @Override
    public int compareTo(Interval i) {
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

public class teaparty {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        br.readLine();
        String[] secondLine = br.readLine().split(" ");
        long A = Long.parseLong(secondLine[0]), B = Long.parseLong(secondLine[1]), M = Long.parseLong(secondLine[2]);
        int Q = Integer.parseInt(secondLine[3]);
        // a point is only contained in one interval at any point of time
        TreeSet<Interval> intervals = new TreeSet<>();
        HashMap<Long,Long> positions = new HashMap<>();
        for (int i = 0; i < Q; i++) {
            String[] line = br.readLine().split(" ");
            long X = Long.parseLong(line[1]);
            long s = (A * X + B) % M;
            if (Integer.parseInt(line[0]) == 1) {
                Interval v = new Interval(s, s), a = intervals.floor(v), b = intervals.higher(v);
                // check if s is contained within an existing interval
                boolean isContained = (a != null && a.getEnd() >= s) || (b != null && b.getStart() <= s);
                long insertionPoint = s;
                if (!isContained) {
                    // merge with lower intervals, this occurs at most once
                    if (a != null && a.getEnd() == v.getStart() - 1) {
                        intervals.remove(a);
                        v = new Interval(a.getStart(), v.getEnd());
                    }
                    // merge with intervals above, this occurs at most once
                    if (b != null && b.getStart() == v.getEnd() + 1) {
                        intervals.remove(b);
                        v = new Interval(v.getStart(), b.getEnd());
                    }
                    intervals.add(v);
                    // pw.printf("a = %s, b = %s\n",a,b);
                } else {
                    // find interval containing s
                    Interval c = intervals.lower(new Interval(s, M));
                    // be careful of edge case for wrap around
                    if (c.getEnd() == M - 1) {
                        Interval L = intervals.lower(new Interval(0, M));
                        Interval H = null;
                        if (L != null) {
                            insertionPoint = L.getEnd() + 1;
                            intervals.remove(L);
                            H = new Interval(0, insertionPoint);
                        } else {
                            insertionPoint = 0;
                            H = new Interval(0, insertionPoint);
                        }
                        // merge with higher interval if necessary
                        Interval T = intervals.higher(H);
                        // merge with intervals above, this occurs at most once
                        if (T != null && T.getStart() == H.getEnd() + 1) {
                            intervals.remove(T);
                            H = new Interval(H.getStart(), T.getEnd());
                        }
                        intervals.add(H);
                    } else {
                        insertionPoint = c.getEnd() + 1;
                        intervals.remove(c);
                        Interval t = new Interval(c.getStart(), insertionPoint);
                        Interval T = intervals.higher(t);
                        // merge with intervals above, this occurs at most once
                        if (T != null && T.getStart() == t.getEnd() + 1) {
                            intervals.remove(T);
                            t = new Interval(t.getStart(), T.getEnd());
                        }
                        intervals.add(t);
                    }
                }
                positions.put(X, insertionPoint);
                pw.println(insertionPoint);
            } else {
                // update positions hashtable
                Long p = positions.get(X);
                positions.remove(X);
                // find interval containing p, guaranteed to exist
                Interval c = intervals.floor(new Interval(p, M));
                intervals.remove(c);
                Long a = c.getStart(), b = c.getEnd();
                // break up the interval
                if (p > a) intervals.add(new Interval(a, p - 1));
                if (p < b) intervals.add(new Interval(p + 1, b));
            }
            // pw.printf("intervals = %s, positions = %s\n", intervals, positions);
        } 
        br.close();
        pw.close();
    }
}