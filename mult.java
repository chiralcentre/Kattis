import java.util.*;

public class mult {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        List<Integer> round = new ArrayList<Integer>();
        for (int i = 0; i < n; i++){
            int num = s.nextInt();
            if (round.isEmpty()){round.add(num);}
            else {
                if (num%round.get(0) == 0){
                    System.out.println(num);
                    round.clear();
                }
                else {round.add(num);}
            }
        }
        s.close();
    }
}
