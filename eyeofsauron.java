import java.util.*;

public class eyeofsauron {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String drawing = s.nextLine().strip();
        int left = drawing.indexOf("("), right = drawing.length() - 1 - drawing.indexOf(")");
        System.out.println(left != right ? "fix" : "correct");
        s.close();
    }
}
