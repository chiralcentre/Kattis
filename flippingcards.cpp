#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

typedef vector<int> vi;


class UnionFind {
    private:
    vi p, rank, setSize;
    int numSets;

    public:
    UnionFind(int N) {
        p.assign(N,0);
        for (int i = 0; i < N; i++) p[i] = i;
        setSize.assign(N,1);
        rank.assign(N,0);
        numSets = N;
    }

    int findSet(int i) {
        if (p[i] == i) return i;
        else {
            p[i] = findSet(p[i]);
            return p[i];
        }
    }

    bool isSameSet(int i, int j) {return findSet(i) == findSet(j);}

    bool unionSet(int i, int j) {
        int x = findSet(i), y = findSet(j);
        if (x != y) {
            if (rank[x] > rank[y]) swap(x,y);
            p[x] = y;
            if (rank[x] == rank[y]) rank[y]++;
            setSize[y] += setSize[x];
            setSize[x] = 0;
            numSets--;
        }
        if (setSize[y] > 0) {
            setSize[y]--;
            return true;
        } else return false;
    }

    int numOfDisjointSets() {return numSets;}

    int sizeOfSet(int i) {return setSize[findSet(i)];}
};

int main() {
    int T; scanf("%d",&T);
    while (T--) {
        int n; scanf("%d",&n);
        UnionFind UFDS(2 * n); // maximum value of card is 2n
        bool possible = true;
        for (int i = 0; i < n; i++) {
            int u,v; scanf("%d %d",&u,&v);
            if (!UFDS.unionSet(u - 1, v - 1)) possible = false;
        }
        printf(possible ? "possible\n" : "impossible\n");
    }
    return 0;
}