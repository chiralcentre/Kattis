import java.io.*;
// taken from lecture slides
class UnionFind {                                              
  public int[] p,rank;

  public UnionFind(int N) {
    p = new int[N];
    rank = new int[N];
    for (int i = 0; i < N; i++) {
      p[i] = i;
      rank[i] = 0;
    }
  }

  public int findSet(int i) { 
    if (p[i] == i) return i;
    else {
      p[i] = findSet(p[i]);
      return p[i]; 
    } 
  }

  public Boolean isSameSet(int i, int j) {return findSet(i) == findSet(j); }

  public void unionSet(int i, int j) { 
    if (!isSameSet(i, j)) { 
      int x = findSet(i), y = findSet(j);
      // rank is used to keep the tree short
      if (rank[x] > rank[y]) 
      	p[y] = x;
      else { 
      	p[x] = y;
        if (rank[x] == rank[y]) 
          rank[y] = rank[y]+1; 
      } 
    } 
  }
}

public class swaptosort {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]), K = Integer.parseInt(firstLine[1]);
        UnionFind UFDS = new UnionFind(N);
        for (int i = 0; i < K; i++){
            String[] line = br.readLine().split(" ");
            int a = Integer.parseInt(line[0]), b = Integer.parseInt(line[1]);
            UFDS.unionSet(a-1, b-1);
        }
        // array can only be sorted in increasing order if j and N-j-1 are in the same set for all j
        boolean possible = true;
        for (int j = 0; j < N; j++){
            if (UFDS.findSet(j) != UFDS.findSet(N-j-1)){
                possible = false;
                break;
            }
        }
        pw.println(possible ? "Yes" : "No");
        br.close();
        pw.close();
    }
}
