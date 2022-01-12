import java.util.Scanner;

class printer {
    public static double log2(int N){
        double result = Math.log(N)/Math.log(2);
        return result;
    }
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        System.out.println((int) Math.ceil(log2(N)) + 1);
        s.close();
    }
}
