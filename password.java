import java.io.*;
import java.util.Arrays;

public class password {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = Integer.parseInt(br.readLine());
        double[] probabilities = new double[n];
        for (int i = 0; i < n; i++){
            String[] line = br.readLine().split(" ");
            probabilities[i] = Double.parseDouble(line[1]); // actual password is not needed
        }
        Arrays.sort(probabilities);
        double expectation = 0;
        // crack the passwords using the passwords with the highest probability first
        // number of attempts increase according to how many passwords have been tried
        for (int i = n-1; i >= 0; i--) expectation += probabilities[i]*(n-i);
        pw.println(expectation);
        br.close();
        pw.close();
    }
}
