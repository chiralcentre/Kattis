import java.io.*;

public class skruop {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = Integer.parseInt(br.readLine()), volume = 7; //starting volume is 7
        for (int i = 0; i < n; i++){
            String line = br.readLine().strip();
            if (line.equals("Skru op!") && volume < 10) volume += 1;
            if (line.equals("Skru ned!") && volume > 0) volume -= 1;
        }
        pw.println(volume);
        br.close();
        pw.close();
    }
}
