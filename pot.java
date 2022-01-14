import java.util.Scanner;

public class pot {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine()), total = 0;
        for (int i = 0; i < n; i++){
            String line = s.nextLine().strip();
            int x = Integer.parseInt(line.substring(0,line.length()-1)), y = Integer.parseInt(line.substring(line.length()-1,line.length()));
            total += (int) Math.pow(x,y);
        }
        System.out.println(total);
        s.close();
    }
}
