import java.util.*;

public class aprizenoonecanwin{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String[] firstLine = s.nextLine().split(" ");
        int n = Integer.parseInt(firstLine[0]), X = Integer.parseInt(firstLine[1]), items = 1;
        int[] costs = new int[n];
        for (int i = 0; i < n; i++){costs[i] = s.nextInt();}
        Arrays.sort(costs);
        for (int j = 1; j < n; j++){
            if (costs[j] + costs[j-1] <= X) {items += 1;}
            else {break;}
        }
        System.out.println(items);
        s.close();
    }
}