import java.io.*;

public class findingana {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String input = br.readLine().strip();
        int n = 0;
        for (int i = 0; i < input.length(); i++){
            if (input.charAt(i) == 'a'){
                n = i;
                break;
            }
        }
        pw.println(input.substring(n));
        br.close();
        pw.close();
    }
}
