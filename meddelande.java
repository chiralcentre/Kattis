import java.io.*;

public class meddelande {
        
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]), M = Integer.parseInt(firstLine[1]);
        String[] grid = new String[N];
        for (int i = 0; i < N; i++) grid[i] = br.readLine().strip();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (Character.isLetter(grid[i].charAt(j))) {
                    pw.print(grid[i].charAt(j));
                }
            }
        }
        br.close();
        pw.close();
    }
}
