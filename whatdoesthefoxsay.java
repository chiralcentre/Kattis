import java.io.*;
import java.util.*;

public class whatdoesthefoxsay {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++){
            String[] recording = br.readLine().split(" ");
            Set<String> sounds = new HashSet<>();
            while (true){
                String[] line = br.readLine().split(" ");
                if (line.length == 3) {sounds.add(line[2]);}
                else { // what does the fox say? line is last line of test case
                    ArrayList<String> foxSound = new ArrayList<>();
                    for (String s: recording) {if (!sounds.contains(s)) {foxSound.add(s);}} // filter out the sounds of other animals
                    pw.println(String.join(" ",foxSound));
                    break;
                } 
            }
        }
        br.close();
        pw.close();
    }
}
