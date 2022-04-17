import java.io.*;

public class allpairspath {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        boolean first = true;
        while (true){
            String[] firstLine = br.readLine().split(" ");
            int n = Integer.parseInt(firstLine[0]), m = Integer.parseInt(firstLine[1]), q = Integer.parseInt(firstLine[2]);
            if (n == 0 && m == 0 && q == 0) break;
            if (first) first = false;
            else pw.println(); //new line
            // Floyd Warshall's algorithm is used
            int INF = 1000000000; // use 1 billion to represent infinity
            int[][] D = new int[n][n];
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    if (i == j) D[i][j] = 0;
                    else D[i][j] = INF;
                }
            }
            for (int i = 0; i < m; i++){
                String[] line = br.readLine().split(" ");
                int u = Integer.parseInt(line[0]), v = Integer.parseInt(line[1]), w = Integer.parseInt(line[2]);
                D[u][v] = Math.min(w,D[u][v]);
            }
            // first iteration of Floyd Warshall
            for (int k = 0; k < n; k++){
                for (int i = 0; i < n; i++){
                    for (int j = 0; j < n; j++){
                        D[i][j] = Math.min(D[i][j], (D[i][k] == INF || D[k][j] == INF) ? INF : D[i][k] + D[k][j]);
                    }
                }
            }
            // second iteration of Floyd Warshall
            for (int k = 0; k < n; k++){
                for (int i = 0; i < n; i++){
                    for (int j = 0; j < n; j++){
                        if (D[k][k] < 0 && D[i][k] != INF && D[k][j] != INF){ // negative cycles at vertex k
                            D[i][j] = -INF;
                        }   
                    }
                }
            }
            for (int i = 0; i < q; i++){
                String[] line = br.readLine().split(" ");
                int u = Integer.parseInt(line[0]), v = Integer.parseInt(line[1]);
                pw.println(D[u][v] == INF ? "Impossible" : (D[u][v] == -INF ? "-Infinity" : D[u][v]));
            }
        }
        br.close();
        pw.close();
    }
}
