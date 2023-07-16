#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef tuple<int,int,int> iii;
typedef vector<iii> viii;

int T,N,u,v,w;

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

int main() {
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&N);
        UnionFind UFDS(N); viii edges;
        for (int i = 0; i < N - 1; i++) {
            scanf("%d %d %d",&u,&v,&w);
            u--; v--;
            edges.push_back(make_tuple(w,u,v));
        }
        sort(edges.begin(), edges.end());
        ll minWeight = 0;
        for (auto &[w,u,v]: edges) {
            minWeight += w + ll(UFDS.sizeOfSet(u) * UFDS.sizeOfSet(v) - 1) * ll(w + 1);
            UFDS.unionSet(u,v);
        }
        printf("%lld\n",minWeight);
    }
    return 0;
}