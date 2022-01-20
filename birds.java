import java.util.*;

public class birds {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String[] firstLine = s.nextLine().split(" ");
        int L = Integer.parseInt(firstLine[0]), D = Integer.parseInt(firstLine[1]), N = Integer.parseInt(firstLine[2]);
        if (N == 0){System.out.println((int)(L-12)/D + 1);}
        else {
            int[] positions = new int[N];
            for (int i = 0; i < N; i++){positions[i] = Integer.parseInt(s.nextLine());}
            Arrays.sort(positions);
            int extra = (int) (positions[0]-6)/D + (int) (L-6-positions[N-1])/D;
            for (int j = 0; j < N - 1; j++){
                if (positions[j+1] - positions[j] >= 2*D){
                    extra += (int) (positions[j+1] - positions[j])/D - 1;
                }
            }
            System.out.println(extra);
        }
        s.close();
    }
}
