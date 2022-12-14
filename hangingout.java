import java.io.*;

public class hangingout {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int L = Integer.parseInt(firstLine[0]), x = Integer.parseInt(firstLine[1]), people = 0, rejected = 0;
        for (int i = 0; i < x; i++){
            String[] line = br.readLine().split(" ");
            if (line[0].equals("enter")){
                if (people + Integer.parseInt(line[1]) > L){rejected += 1;}
                else {people += Integer.parseInt(line[1]);}
            }
            else {people -= Integer.parseInt(line[1]);} //people are leaving
        }
        pw.println(rejected);
        br.close();
        pw.close();
    }
}
