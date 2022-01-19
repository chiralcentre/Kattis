import java.util.*;

public class bookingaroom {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String[] firstLine = s.nextLine().split(" ");
        int r = Integer.parseInt(firstLine[0]), n = Integer.parseInt(firstLine[1]);
        List<Integer> rooms = new ArrayList<>();
        for (int i = 1; i <= r; i++){rooms.add(i);}
        for (int j = 0; j < n; j++){
            Integer num = Integer.parseInt(s.nextLine()); // an object is created for removal
            rooms.remove(num);
        }
        System.out.println(n == r ? "too late": rooms.get(0)); // rooms list will at least have one room number if n < r
        s.close();
    }
}
