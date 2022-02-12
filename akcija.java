import java.io.*;
import java.util.*;

public class akcija {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = Integer.parseInt(br.readLine());
        long minimalPrice = 0;
        ArrayList<Integer> prices = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) prices.add(Integer.parseInt(br.readLine()));
        Collections.sort(prices);
        while (prices.size() >= 3){
            int a = prices.remove(prices.size()-1), b = prices.remove(prices.size()-1);
            prices.remove(prices.size()-1);
            minimalPrice += a + b;
        }
        while (prices.size() > 0) minimalPrice += prices.remove(prices.size()-1);
        pw.println(minimalPrice);
        br.close();
        pw.close();
    }
}
