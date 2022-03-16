import java.io.*;
import java.util.*;

class Song{
    private long quality,index;
    private String title;

    public Song(long quality, long index, String title){
        this.quality = quality;
        this.index = index;
        this.title = title;
    }

    public long getQuality() {return this.quality;}

    public long getIndex() {return this.index;}

    public String getTitle() {return this.title;}
}

class QualityComparator implements Comparator<Song> {
    // sort by song quality in ascending order, and for songs with same quality, sort by order in reverse order
	public int compare(Song s1, Song s2) {
        return (Long.compare(s1.getQuality(), s2.getQuality()) != 0 ? Long.compare(s1.getQuality(), s2.getQuality()): -Long.compare(s1.getIndex(),s2.getIndex()));
    }

	public boolean equals(Object obj) {return this == obj;}
}

public class zipfsong {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        QualityComparator qComp = new QualityComparator();
        String[] firstLine = br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]), m = Integer.parseInt(firstLine[1]);
        ArrayList<Song> songs = new ArrayList<>();
        for (long i = 1; i < n+1; i++){
            String[] line = br.readLine().split(" ");
            long f = Long.parseLong(line[0]); String s = line[1];
            songs.add(new Song(f*i,i,s)); //Zi is proportional to 1/i, so f/Zi is proportional to f*i
        }
        // O(n log n) - sort by quality in ascending order, then sort by order of appearance in reverse so earliest song will be popped first
        Collections.sort(songs,qComp);
        for (int j = 0; j < m; j++) {pw.println(songs.remove(songs.size()-1).getTitle());}
        br.close();
        pw.close();
    }
}
