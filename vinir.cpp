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
        int x = findSet(i), y = findSet(j);
        if (x != y) {
            if (rank[x] > rank[y]) swap(x,y);
            p[x] = y;
            if (rank[x] == rank[y]) rank[y]++;
            setSize[y] += setSize[x];
            setSize[x] = 0;
            numSets--;
        }
    }

    int numOfDisjointSets() {return numSets;}

    int sizeOfSet(int i) {return setSize[findSet(i)];}
};

int N,Q,q,a,b;

int main() {
    scanf("%d %d",&N,&Q);
    UnionFind UFDS(N);
    for (int i = 0; i < Q; i++) {
        scanf("%d",&q);
        if (q == 1) {
            scanf("%d %d",&a,&b);
            UFDS.unionSet(a - 1, b - 1);
        } else {
            scanf("%d",&a);
            printf("%d\n",UFDS.sizeOfSet(a - 1) - 1);
        }
    }
    return 0;
}