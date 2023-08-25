import java.util.*;

public class peasoup {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
        List<String> restaurants = new ArrayList<String>();
        for (int i = 0; i < n; i++){
            int k = Integer.parseInt(s.nextLine());
            String name = s.nextLine().strip();
            Boolean pancakes = false, peasoup = false;
            for (int j = 0; j < k; j++){
                String menuItem = s.nextLine().strip();
                if (menuItem.equals("pancakes")){pancakes = true;}
                else if (menuItem.equals("pea soup")){peasoup = true;}
            }
            if (pancakes && peasoup){restaurants.add(name);}
        }
        System.out.println(restaurants.size() > 0 ? restaurants.get(0) : "Anywhere is fine I guess");
        s.close();
    }
}
