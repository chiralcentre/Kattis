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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,B,M; cin >> N >> B >> M;
    vi boatOwners;
    for (int i = 0; i < B; i++) {
        int p; cin >> p;
        boatOwners.push_back(--p);
    }
    UnionFind UFDS(N);
    for (int i = 0; i < M; i++) {
        int u,v; cin >> u >> v;
        u--; v--;
        UFDS.unionSet(u,v);
    }
    //find set of all unique representative items in O(N)
    unordered_set<int> repr;
    for (int i = 0; i < N; i++) repr.insert(UFDS.findSet(i));
    int ans = UFDS.numOfDisjointSets();
    for (int b: boatOwners) { // O(B)
        int j = UFDS.findSet(b);
        if (repr.find(j) != repr.end()) {
            ans--; repr.erase(j);
        }
    }
    cout << ans << "\n";
    return 0;
}