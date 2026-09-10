import java.io.*;
import java.util.*;

public class racinggame {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int Q = Integer.parseInt(br.readLine());
        long offset = 0;
        TreeSet<LongPair> timings = new TreeSet<>();
        for (int i = 0; i < Q; i++) {
            String[] line = br.readLine().split(" ");
            int first = Integer.parseInt(line[0]);
            long second = Long.parseLong(line[1]);
            if (first == 1) {
                timings.add(new LongPair(second - offset, Long.valueOf(i)));
            } else if (first == 2) {
                offset += second;
            } else {
                Iterator<LongPair> it = timings.iterator();
                LongPair current = null;
                for (int j = 0; j < second && it.hasNext(); j++) current = it.next();
                pw.println(current.first() + offset);
            }
        }
        br.close();
        pw.close();
    }
}

class LongPair implements Comparable<LongPair> {// stores coordinates
    private Long _first, _second;
  
    public LongPair(Long f, Long s) {
      _first = f;
      _second = s;
    }
  
    public int compareTo(LongPair o) {
      if (!this.first().equals(o.first())) return (this.first() - o.first() > 0) ? 1 : -1;
      else return (this.second() - o.second() > 0) ? 1 : -1;
    }
  
    Long first() {return _first;}
  
    Long second() {return _second;}
}
