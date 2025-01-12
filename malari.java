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

public class malari {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine =  br.readLine().split(" ");
        long N = Long.parseLong(firstLine[0]); int M = Integer.parseInt(firstLine[1]);
        long covered = 0;
        TreeSet<Interval> intervals = new TreeSet<Interval>();
        for (int i = 0; i < M; i++) {
            String[] line = br.readLine().split(" ");
            long s = Long.parseLong(line[0]), e = Long.parseLong(line[1]);
            Interval v = new Interval(s, e), a = intervals.lower(v);
            if (!intervals.contains(v)) {
                covered += e - s + 1;
                // merge with lower intervals
                while (a != null && a.getEnd() >= s) {
                    long ns = a.getStart(), ne = a.getEnd();
                    s = v.getStart(); e = v.getEnd();
                    intervals.remove(a);
                    if (e >= ne) {
                        covered -= ne - s + 1;
                        a = intervals.lower(v);
                    } else {
                        covered -= e - s + 1;
                        a = intervals.lower(a);
                    }
                    v = new Interval(ns, Math.max(ne,e));
                }
                a = intervals.higher(v);
                // merge with intervals above
                while (a != null && a.getStart() <= e) {
                    long ns = a.getStart(), ne = a.getEnd();
                    s = v.getStart(); e = v.getEnd();
                    intervals.remove(a);
                    if (ne >= e) { 
                        covered -= e - ns + 1;
                        v = new Interval(s, ne);
                        a = intervals.higher(v);
                    } else {
                        covered -= ne - ns + 1;
                        a = intervals.higher(a);
                    }    
                }
                intervals.add(v);
            }
        }
        pw.println(covered);
        pw.printf(covered * 2 > N ? "The Mexicans took our jobs! Sad!\n" : "The Mexicans are Lazy! Sad!\n");
        br.close();
        pw.close();
    }
}