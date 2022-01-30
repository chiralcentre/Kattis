import java.util.*;

public class skener {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int[] intArray = Arrays.stream(s.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int R = intArray[0], C = intArray[1], ZR = intArray[2], ZC = intArray[3];
        String[][] matrix = new String[R*ZR][C*ZC];
        for (int i = 0; i < R; i++){
            String line = s.nextLine().strip();
            for (int j = 0; j < C; j++){
                String symbol = line.substring(j,j+1);
                for (int k = ZR*i; k < ZR*i + ZR; k++){for (int m = ZC*j; m < ZC*j + ZC; m++){matrix[k][m] = symbol;}}
            }
        }
        for (String[] row: matrix){
            for (String symbol: row){System.out.print(symbol);}
            System.out.println(); //new line
        }
        s.close();
    }
}
