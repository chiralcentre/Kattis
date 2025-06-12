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

public class ccclager {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine =  br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]), M = Integer.parseInt(firstLine[1]);
        String[] participants = new String[N];
        for (int i = 0; i < N; i++) participants[i] = br.readLine().strip();
        ArrayList<Interval> intervals = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            String[] line = br.readLine().split(" ");
            long s = Long.parseLong(line[0]), e = Long.parseLong(line[1]);
            intervals.add(new Interval(s, e));
        }
        Collections.sort(intervals);
        Interval window = intervals.get(0);
        TreeSet<Interval> tree = new TreeSet<>();
        for (int i = 1; i < M; i++) {
            Interval curr = intervals.get(i);
            if (curr.getStart() <= window.getEnd() + 1) window = new Interval(window.getStart(), Math.max(window.getEnd(), curr.getEnd()));
            else { 
                tree.add(window);
                window = curr;
            }
        }
        tree.add(window);
        long ans = 0;
        for (int i = 0; i < N; i++) {
            String[] p = participants[i].split(" ");
            long d = Long.parseLong(p[1]);
            Interval v = new Interval(d, (long) 1e10), a = tree.lower(v);
            if (a == null || a.getEnd() < d) {
                ans++;
                if (p[0].equals("Joshua") || p[0].equals("Gustav")) ans++;
            }
        }
        pw.println(ans);
        br.close();
        pw.close();
    }
}