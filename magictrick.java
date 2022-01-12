import java.util.HashSet;
import java.util.Scanner;

public class magictrick {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String s = input.next();
        char[] word = s.toCharArray();
        HashSet<Character> unique = new HashSet<Character>(); // equivalent of sets in python
        for (int i = 0; i < word.length; i++){
            unique.add(word[i]);
        }
        System.out.println(word.length == unique.size() ? 1 : 0);
    }
}
