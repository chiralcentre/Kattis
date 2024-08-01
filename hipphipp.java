import java.io.*;

public class hipphipp {
    public static void main(String[] args) {
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        for (int i = 0; i < 20; i++) pw.println("Hipp hipp hurra!");
        pw.close();
    }
}