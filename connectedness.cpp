#include <bits/stdc++.h>

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

    void unionSet(int i, int j) {
        if (!isSameSet(i,j)) {
            int x = findSet(i), y = findSet(j);
            if (rank[x] > rank[y]) swap(x,y);
            p[x] = y;
            if (rank[x] == rank[y]) rank[y]++;
            setSize[y] += setSize[x];
            numSets--;
        }
    }

    int numOfDisjointSets() {return numSets;}

    int sizeOfSet(int i) {return setSize[findSet(i)];}
};

int N,M,u,v;

int main() {
    scanf("%d %d",&N,&M);
    UnionFind UFDS(N);
    for (int i = 0; i < M; i++) {
        scanf("%d %d",&u,&v);
        u--; v--;
        UFDS.unionSet(u,v);
        if (UFDS.numOfDisjointSets() == 1) {
            printf("%d\n", i + 1);
            return 0;
        }
    }
    N > 1 ? printf("-1\n") : printf("0\n");
    return 0;
}