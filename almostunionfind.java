import java.io.*;

class UFDS {                                              
    public int[] p,p2,rank,numElems;
    public long[] total;

    public UFDS (int N) {
        p = new int[N]; p2 = new int[N]; rank = new int[N];
        numElems = new int[N]; total = new long[N];
        for (int i = 0; i < N; i++) {
            p[i] = i;
            p2[i] = i; //keeps track of original parent when a move command is made
            rank[i] = 0;
            numElems[i] = 1; //keeps track of number of elements in each disjoint set
            total[i] = i; //keeps track of sum of elements in each each disjoint set
        }
    }

    public int findSet(int i) { 
        int a = p2[i];
        int b = p[a];
        while (a != b) {//while parent of i and parent of parent of i do not match
            p[a] = p[b];
            a = p[a];
            b = p[a];
        }
        return a;
    }

    public Boolean isSameSet(int i, int j) {return findSet(i) == findSet(j);}

    public void unionSet(int i, int j) { 
        if (!isSameSet(i, j)) { 
            int x = findSet(i), y = findSet(j);
            // union by rank
            if (rank[x] > rank[y]){// swap x and y if rank[x] > rank[y] to shorten code 
                int temp = x;
                x = y;
                y = temp;
            }
            p[y] = x;
            numElems[x] += numElems[y];
            numElems[y] = 0; 
            total[x] += total[y];
            total[y] = 0;
        }
    }

    public void move(int i, int j){
        if (!isSameSet(i,j)){
            int x = findSet(i), y = findSet(j);
            numElems[x] -= 1; numElems[y] += 1;
            total[x] -= i; total[y] += i;
            p2[i] = y; //keep track of original parent
        }
    }

    public int numOfElements(int i) {return numElems[findSet(i)];}
    // number of elements is added back to offset zero indexing
    public long findSum(int i) {return total[findSet(i)] + numOfElements(i);}

}

public class almostunionfind {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        while (true){
            try {
                String[] s = br.readLine().split(" ");
                int N = Integer.parseInt(s[0]), M = Integer.parseInt(s[1]);
                UFDS disjointSets = new UFDS(N);
                for (int i = 0; i < M; i++){
                    String[] command = br.readLine().split(" ");
                    if (command[0].equals("3")) {
                        int x = Integer.parseInt(command[1]) - 1; //-1 for zero indexing
                        pw.printf("%d %d\n",disjointSets.numOfElements(x),disjointSets.findSum(x));
                    } 
                    else {
                        int x = Integer.parseInt(command[1]) - 1, y = Integer.parseInt(command[2]) - 1; //-1 for zero indexing
                        if (command[0].equals("1")) {disjointSets.unionSet(x, y);}
                        else {disjointSets.move(x, y);}
                    }
                }
            }
            catch (Exception e){ // check for EOF error
                break;
            }
        }
        br.close();
        pw.close();
    }
}

