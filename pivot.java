import java.util.*;
import java.io.*;

public class pivot {
    // finds indices of elements that are larger than all elements on left
    // PRE-COND: 3 <= n <= 100000, arr contains n distinct 32-bit signed integers
    // POST-COND: a HashSet containing the indices of elements that are larger than all elements on left,
    // size of HashSet <= n, indices are unique in HashSet
    public static HashSet<Integer> findLocalMaximums(int[] arr, int n) {
        HashSet<Integer> maximum = new HashSet<Integer>();
        int largest = -2147483647;
        //possible local maximums
        for (int i = 0; i < n; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
                maximum.add(i);
            }
        }
        return maximum;
    }

    // finds indices of elements that are <= all elements on right
    // PRE-COND: 3 <= n <= 100000, arr contains n distinct 32-bit signed integers
    // POST-COND: a HashSet containing the indices of elements that are <= all elements on right,
    // size of HashSet <= n, indices are unique in HashSet
    public static HashSet<Integer> findLocalMinimums (int[] arr, int n) {
        HashSet<Integer> minimum = new HashSet<Integer>();
        int smallest = 2147483647;
        // possible local minimums
        for (int i = n - 1; i > -1; i--) {
            if (arr[i] <= smallest) {
                smallest = arr[i];
                minimum.add(i);
            }
        }
        return minimum;
    }

    // calculate the number of possible pivots for partitions
    // PRE-COND: localMax contains the indices of elements that are larger than all elements on left,
    // size of HashSet <= n, indices are unique in HashSet
    // localMin contains the indices of elements that are <= all elements on right,
    // size of HashSet <= n, indices are unique in HashSet
    // POST-COND: returns integer representing number of possibl pivots, 0 <=  integer <= n
    public static int findPivots(HashSet<Integer> localMax, HashSet<Integer> localMin) {
        int pivots = 0;
        for (int p: localMax) {
            if (localMin.contains(p)) {
                pivots++;
            }
        }
        return pivots;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n =  Integer.parseInt(br.readLine());
        String[] secondLine = br.readLine().split(" ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(secondLine[i]);
        pw.println(findPivots(findLocalMaximums(arr, n), findLocalMinimums(arr, n)));
        br.close();
        pw.close();
    }
}
