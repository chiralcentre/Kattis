import java.util.*;
import java.io.*;

/*If k = 0, we can solve the problem by doing the following:
For each person, create two events, arrival and departure
Sort all events, and sort arrivals before departures
counter = 0
for each event: if event is arrival, counter += 1, else counter -= 1
keep track of maximum value of counter
if k > 0, it is equivalent to staying for 0 seconds while everyone else stays for k seconds longer
 */
class Event implements Comparable<Event>{
    private int time;
    private int event; // use 0 to represent arrival and 1 to represent departure

    public Event(int time, int event){
        this.time = time;
        this.event = event;
    }

    public int getTime() {return this.time;}

    public int getEvent() {return this.event;}

    public int compareTo(Event e){
        if (this.time != e.time) return this.time - e.time;
        return this.event - e.event;
    }
}

public class alehouse {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine =  br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]), k = Integer.parseInt(firstLine[1]);
        ArrayList<Event> events = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            int a = Integer.parseInt(line[0]), b = Integer.parseInt(line[1]) + k;
            events.add(new Event(a,0)); events.add(new Event(b,1));
        }
        Collections.sort(events);
        int counter = 0, highest = 0;
        for (Event e: events){
            counter += (e.getEvent() == 0 ? 1 : -1);
            if (counter > highest) highest = counter;
        }
        pw.println(highest);
        br.close();
        pw.close();
    }
}