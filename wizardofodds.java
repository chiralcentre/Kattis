import java.util.*;

public class wizardofodds {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        double N = s.nextDouble(), K = s.nextDouble();
        // questions can be used to conduct binary search
        System.out.println(Math.pow(2,K) >= N ? "Your wish is granted!":"You will become a flying monkey!");
        s.close();
    }
}

