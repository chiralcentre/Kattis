import java.io.*;
import java.util.*;

class Coin {
    private final int conv;
    private final int infotech;
  
    public Coin(int conv, int infotech) {
        this.conv = conv;
        this.infotech = infotech;
    }

    public int getConv() {
        return this.conv;
    }

    public int getInfotech() {
        return this.infotech;
    }
}

class CoinCounter {
    private final Coin coin;
    private final int moves;
  
    public CoinCounter(Coin coin, int moves) {
        this.coin = coin;
        this.moves = moves;
    }
    
    public Coin getCoin() {return this.coin;}

    public int getMoves() {return this.moves;}
}


public class ecoins {
    public static String BFS(Coin[] coins, int s) {
        // to reach a modulus of s, conv and infotech values cannot exceed s
        boolean[][] visited = new boolean[s][s];
        Queue<CoinCounter> frontier = new ArrayDeque<CoinCounter>();
        int e = s * s; // e is square of ending modulus
        for (Coin c: coins) {
            int a = c.getConv(), b = c.getInfotech();
            int squaredModulus = getSquaredModulus(a,b);
            if (squaredModulus < e && !visited[a][b]) {
                visited[a][b] = true;
                frontier.add(new CoinCounter(c, 1));
            } else if (squaredModulus == e) return "1";
        }
        while (!frontier.isEmpty()) {
            CoinCounter temp = frontier.poll();
            int a = temp.getCoin().getConv(), b = temp.getCoin().getInfotech();
            for (Coin c: coins) {
                int x = c.getConv(), y = c.getInfotech();
                int squaredModulus = getSquaredModulus(a + x,b + y);
                if (squaredModulus < e && !visited[a + x][b + y]) {
                    visited[a + x][b + y] = true;
                    frontier.add(new CoinCounter(new Coin(a + x, b + y), temp.getMoves() + 1));
                } else if (squaredModulus == e) return String.format("%d",temp.getMoves() + 1);
            }
        }
        return "not possible";
    }

    public static int getSquaredModulus(int conv, int infotech) {
        return conv * conv + infotech * infotech;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            if (i > 0) br.readLine(); //read in blank line between test cases
            String[] firstLine = br.readLine().split(" ");
            int m = Integer.parseInt(firstLine[0]), s = Integer.parseInt(firstLine[1]);
            Coin[] coins = new Coin[m];
            for (int j = 0; j < m; j++) {
                String[] coinDesc = br.readLine().split(" ");
                coins[j] = new Coin(Integer.parseInt(coinDesc[0]),Integer.parseInt(coinDesc[1]));
            }
            pw.print(BFS(coins,s) + "\n");
        }
        br.close();
        pw.close();
    }
}