import java.io.*;

public class fluortanten {
    /* PRE COND: secondLine must contain N space separated integers in the range [-1000,1000]
    representing the happiness of each child
    */
    /* POST COND: an integer array of N - 1 integers in the range [-1000,1000] will be returned.
    The integer array does not contain Bjorn's happiness (0).
    */ 
    public static int[] processQueue(int N, String[] secondLine) {
        int[] sequence = new int[N-1];
        boolean foundBjorn = false;
        for (int i = 0; i < N; i++) {
            int happiness = Integer.parseInt(secondLine[i]);
            // if Bjorn is found, set boolean counter to true so that he will not be inserted into array
            if (happiness == 0) foundBjorn = true;
            else {
                // if Bjorn has been found, shift the index to the left by one 
                if (foundBjorn) sequence[i-1] = happiness;
                else sequence[i] = happiness;
            }
        }
        return sequence;
    }
    /* PRE COND: An integer array of N - 1 integers in the range [-1000,1000] will be provided as the parameter.
    The integer array does not contain Bjorn's happiness (0). 
    */
    /* POST COND: An integer representing the maximum happiness out of all possible permutations of 
    Bjorn insertion spots will be returned. The integer may exceed a 32 bit int data type.
    */ 
    public static long solve(int N, int[] sequence) {
        long maxHappiness = 0;
        if (N == 1) return maxHappiness;
        else {
            // prefixSumArray[i] = sum of elements from 0 to ith index inclusive
            // indexSumArray[i] = sum of elements from 0 to ith index inclusive multiplied by i + 1 for each element
            long [] prefixSumArray = new long[N-1], indexSumArray = new long[N-1];
            long prefixSum = 0, indexSum = 0;
            for (int i = 0; i < N-1; i++) {
                prefixSum += sequence[i]; indexSum += (i+1)*sequence[i];
                prefixSumArray[i] = prefixSum; indexSumArray[i] = indexSum;
            }
            //Insertion of Bjorn at last spot
            maxHappiness = indexSumArray[N-2];
            //Insert Bjorn at every position except last spot
            for (int i = 0; i < N - 1; i++) {
                // calculate difference if Bjorn is inserted
                long pSum = i > 0 ? prefixSumArray[N-2] - prefixSumArray[i-1] : prefixSumArray[N-2];
                long tempHappiness = indexSumArray[N-2] + pSum;
                maxHappiness = Math.max(maxHappiness,tempHappiness);
            }
            return maxHappiness;
        }
    }
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine());
        String[] secondLine = br.readLine().split(" ");
        int[] sequence = processQueue(N, secondLine);
        pw.println(solve(N, sequence));
        br.close();
        pw.close();
    }
}
