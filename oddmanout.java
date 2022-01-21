import java.util.*;

public class oddmanout {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int N = Integer.parseInt(s.nextLine());
        for (int i = 0; i < N; i++){
            int G = Integer.parseInt(s.nextLine());
            String[] guests = s.nextLine().split(" ");
            Hashtable<String,Integer> dict1 = new Hashtable<String,Integer>();
            for (int j = 0; j < G; j++){
                if (!dict1.containsKey(guests[j])){dict1.put(guests[j],1);}
                else{dict1.put(guests[j],dict1.get(guests[j])+1);}
            }
            Set<String> keys = dict1.keySet();
            for (String key : keys){
                if (dict1.get(key) == 1){
                    System.out.printf("Case #%d: %s%n",i+1,key);
                    break;
                }
            }
        }
        s.close();
    }
}
