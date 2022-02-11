import java.io.*;

public class sodaslurper {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int e = Integer.parseInt(firstLine[0]), f = Integer.parseInt(firstLine[1]), c = Integer.parseInt(firstLine[2]);
        int bottles = e + f, sodas = 0;
        while (bottles >= c){
            int bottlesDrank = bottles/c;
            bottles %= c;
            sodas += bottlesDrank;
            bottles += bottlesDrank;
        }
        pw.println(sodas);
        br.close();
        pw.close();
    }
}
