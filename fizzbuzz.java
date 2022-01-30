import java.util.Scanner;

public class fizzbuzz {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int X = s.nextInt(), Y = s.nextInt(), N = s.nextInt();
        for (int i = 1; i <= N; i++){
            if (i%X == 0 && i%Y == 0){System.out.println("Fizzbuzz");}
            else if (i%X != 0 && i%Y == 0){System.out.println("Buzz");}
            else if (i%X == 0 && i%Y != 0){System.out.println("Fizz");}
            else {System.out.println(i);}
        }
        s.close();
    }
}
