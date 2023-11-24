#include <bits/stdc++.h>
#include <queue>
#include <bitset>

using namespace std;

typedef pair<int,int> ii;
typedef tuple<int,int,int> iii;
typedef vector<ii> vii;


bitset<250000> bs;
const int INF = 1000000000, H = 250000, L = 500;
int r,c,n,grid[500][500],D[500][500][11],x[3] = {0,-1,1},y[3] = {1,1,1};

int compress(int u, int v) {return u * L + v;}

int three_hash(int u, int v, int w) {return u * H + v * L + w;}

iii dehash(int v) {return {v / H, (v % H) / L, (v % H) % L};}

bool inRange(int a, int b, int c) {return a <= b && b <= c;}

vii possiblepositions(int i, int j, int r, int c) {
    vii pos;
    for (int k = 0; k < 3; k++) {
        if (inRange(0, i + x[k], r - 1) && inRange(0, j + y[k], c - 1) && grid[i + x[k]][j + y[k]] != -1) pos.push_back({i + x[k], j + y[k]});
    }
    return pos;
}

// perform modified Djikstra in O(nrc log nrc)
int solve(int r, int c, int n) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            for (int k = 0; k <= n; k++) D[i][j][k] = INF;
        }
    }
    priority_queue<ii,vii,greater<ii>> pq;
    for (int i = 0; i < r; i++) {
        if (grid[i][0] != -1) {
            D[i][0][n] = grid[i][0];
            pq.emplace(D[i][0][n], three_hash(i,0,n));
        }
    }
    while (!pq.empty()) {
        auto [d,u] = pq.top(); pq.pop();
        auto [i,j,l] = dehash(u);
        if (j == c - 1 && l == 0) return d;
        if (d == D[i][j][l]) {
            for (auto [a,b] : possiblepositions(i,j,r,c)) {
                if (bs.test(compress(a,b))) {
                    if (l > 0 && D[a][b][l - 1] > d + grid[a][b]) {
                        D[a][b][l - 1] = d + grid[a][b];
                        pq.emplace(D[a][b][l - 1],three_hash(a,b,l - 1));
                    }
                } else if (D[a][b][l] > d + grid[a][b]) {
                    D[a][b][l] = d + grid[a][b];
                    pq.emplace(D[a][b][l],three_hash(a,b,l));
                }
            }
        }
    }
    return -1;
}



int main() {
    scanf("%d %d %d",&r,&c,&n);
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) scanf("%d",&grid[i][j]);
    }
    int visited = 0;
    for (int i = 1; i < r - 1; i++) {
        for (int j = 1; j < c - 1; j++) {
            if (grid[i][j] == -1 || grid[i - 1][j] == -1 || grid[i + 1][j] == -1 || grid[i][j - 1] == -1 || grid[i][j + 1] == -1) continue;
            if (grid[i][j] > grid[i][j - 1] && grid[i][j] > grid[i][j + 1] && grid[i][j] < grid[i - 1][j] && grid[i][j] < grid[i + 1][j]) {
                bs.set(compress(i,j));
                visited++;
            }
        }
    }
    if (visited < n) printf("impossible\n");
    else {
        int res = solve(r,c,n);
        (res == -1) ? printf("impossible\n") : printf("%d\n",res);
        return 0;
    }
}