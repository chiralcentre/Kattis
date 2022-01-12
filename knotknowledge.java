import java.util.*;

public class knotknowledge {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = Integer.parseInt(input.nextLine());
        String[] s1 = input.nextLine().split(" ");
        String[] s2 = input.nextLine().split(" ");
        List<String> learned = new ArrayList<>(Arrays.asList(s2));
        for (int i = 0; i < n; i++) {
            if (!learned.contains(s1[i])){
                System.out.println(s1[i]);
                break;
            }
        }
        input.close();
    }
}
