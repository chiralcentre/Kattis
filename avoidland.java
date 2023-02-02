import java.io.*;
import java.util.Arrays;

public class avoidland {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine());
        int[] x_coords = new int[N], y_coords = new int[N];
        for (int i = 0; i < N; i++) {
            String[] line = br.readLine().split(" ");
            x_coords[i] = Integer.parseInt(line[0]);
            y_coords[i] = Integer.parseInt(line[1]);
        }
        Arrays.sort(x_coords); Arrays.sort(y_coords);
        long counter = 0;
        for (int i = 0; i < N; i++) counter += Math.abs(i + 1 - x_coords[i]) + Math.abs(i + 1 - y_coords[i]);
        pw.println(counter);
        br.close();
        pw.close();
    }
}
