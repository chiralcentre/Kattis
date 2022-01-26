import java.util.*;

public class peasoup {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
        List<String> restaurants = new ArrayList<String>();
        for (int i = 0; i < n; i++){
            int k = Integer.parseInt(s.nextLine());
            String name = s.nextLine().strip();
            List<String> menuItems = new ArrayList<String>();
            for (int j = 0; j < k; j++){menuItems.add(s.nextLine().strip());}
            if (menuItems.contains("pancakes") && menuItems.contains("pea soup")){restaurants.add(name);}
        }
        System.out.println(restaurants.size() > 0 ? restaurants.get(0) : "Anywhere is fine I guess");
        s.close();
    }
}
