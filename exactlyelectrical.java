import java.util.Scanner;

public class exactlyelectrical{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a = s.nextInt(), b = s.nextInt(), c = s.nextInt(), d = s.nextInt(), t = s.nextInt();
        int manhattanDistance = Math.abs(a-c) + Math.abs(b-d);
        // print no if manhattan distance > t
        // else, print yes if difference between manhattan distance and electrical charge is a multiple of 2, as this means back and forth trips can be made
        System.out.println(manhattanDistance > t ? "N" : ((t - manhattanDistance)%2 == 0 ? "Y" : "N"));
        s.close();
    }
}