import java.io.*;

public class shatteredcake {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long W = Long.parseLong(br.readLine()), N = Long.parseLong(br.readLine()), totalArea = 0;
        for (int i = 0; i < N; i++){
            String[] line = br.readLine().split(" ");
            totalArea += Long.parseLong(line[0])*Long.parseLong(line[1]);
        }
        System.out.println(totalArea/W);
        br.close();
    }
}
