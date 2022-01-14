import java.util.Scanner;

public class numberfun {
    public static String possible(int a, int b, int c){
        return (a + b == c || b - a == c || a - b == c || a * b == c || (double) a/b == c || (double) b/a == c ? "Possible" : "Impossible");
    }
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
        for (int i = 0; i < n; i++){
            String[] line = s.nextLine().split(" ");
            int x = Integer.parseInt(line[0]), y = Integer.parseInt(line[1]), z = Integer.parseInt(line[2]);
            System.out.println(possible(x,y,z));
        }
        s.close();
    }
}
