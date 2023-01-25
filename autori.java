import java.util.Scanner;

public class autori {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String[] authors = s.nextLine().split("-");
        String initials = "";
        for (int i = 0; i < authors.length; i++){
            initials += authors[i].charAt(0);
        }
        System.out.println(initials);
        s.close();
    }
}
