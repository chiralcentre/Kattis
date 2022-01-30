import java.util.*;

public class apaxiaaans {
    public static void apaxia(String a){
        ArrayList<Character> shortened = new ArrayList<Character>();
        int start = 0, end = a.length()-1;
        while (start <= end){
            char letter = a.charAt(start);
            shortened.add(letter);
            while (start + 1 <= end && a.charAt(start+1) == letter){start += 1;}
            start += 1;
        }
        for (char x: shortened){System.out.print(x);}
    }
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String name = s.nextLine().strip();
        apaxia(name);
        s.close();
    }
}
