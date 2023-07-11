#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

int n,m,s,t,u,v;

struct Matrix {
    vvll mat;
    Matrix(int N) {
        for (int i = 0; i < N; i++) {
            mat.push_back(vll(N,0)); // initialisation
        }
    }
};

Matrix matMul (Matrix a, Matrix b) {
    Matrix ans(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) ans.mat[i][j] = 0;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a.mat[i][j] == 0) continue; //optimisation
            for (int k = 0; k < n; k++) ans.mat[i][k] += a.mat[i][j] * b.mat[j][k];
        }
    }
    return ans;
}

Matrix matPow(Matrix base, ll p) {
    Matrix ans(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) ans.mat[i][j] = (i == j); //prepare identity matrix
    }
    while (p > 0) {
        if (p & 1) ans = matMul(ans,base); // check if p is odd
        base = matMul(base,base);
        p >>= 1;
    }
    return ans;
}

//count number of paths in the undirected graph that are reachable from source s after t steps by multiplying adjacency matrix t times
int main() {
    scanf("%d %d %d %d",&n, &m, &s, &t);
    Matrix base(n);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &u, &v);
        base.mat[u][v] = base.mat[v][u] = 1;
    }
    base = matPow(base, t); // # need to multiply by t times
    ll ans = 0;
    for (int i = 0; i < n; i++) ans += base.mat[s][i];
    printf("%lld\n", ans);
    return 0;
}