import java.io.*;

public class ferryloading4 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int c = Integer.parseInt(br.readLine());
        for (int i = 0; i < c; i++){
            String[] testcase = br.readLine().split(" ");
            int L = Integer.parseInt(testcase[0]), m = Integer.parseInt(testcase[1]);
            L *= 100; // convert metres into centimetres for ease of calculation
            int left = 0, right = 0, leftCrossings = 0, rightCrossings = 0;
            for (int j = 0; j < m; j++){
                String[] line = br.readLine().split(" ");
                int carLength = Integer.parseInt(line[0]);
                if (carLength <= L){// can fit on ferry
                    if (line[1].equals("left")){
                        if (left + carLength > L){
                            left = carLength;
                            leftCrossings += 1;
                        }
                        else {left += carLength;}
                    }
                    else { //right bank
                        if (right + carLength > L){
                            right = carLength;
                            rightCrossings += 1;
                        }
                        else {right += carLength;}
                    }
                }
            }
            if (left > 0){leftCrossings += 1;}
            if (right > 0){rightCrossings += 1;}
            pw.println(leftCrossings <= rightCrossings ? 2*rightCrossings : 2*leftCrossings - 1); // start from left bank
        }
        br.close();
        pw.close();
    }
}
