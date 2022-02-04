import java.io.*;

public class finalexam2 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()), marks = 0;
        String[] answers = new String[n];
        for (int i = 0; i < n; i++){answers[i] = br.readLine().strip();}
        if (n > 1) {
            for (int i = 0; i < n - 1; i++){
                if (answers[i].equals(answers[i+1])){
                    marks += 1;
                }
            }
        }
        System.out.println(marks);
    }
}
