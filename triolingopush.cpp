#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll MOD = 1000000007;
const int MAX_N = 3;

struct Matrix {ll mat[MAX_N][MAX_N] = {{1,1,1},{1,0,0},{0,0,1}};};


Matrix matMul (Matrix a, Matrix b) {
    Matrix ans;
    for (int i = 0; i < MAX_N; i++) {
        for (int j = 0; j < MAX_N; j++) ans.mat[i][j] = 0;
    }
    for (int i = 0; i < MAX_N; i++) {
        for (int j = 0; j < MAX_N; j++) {
            if (a.mat[i][j] == 0) continue; //optimisation
            for (int k = 0; k < MAX_N; k++) {
                ans.mat[i][k] += (a.mat[i][j] % MOD) * (b.mat[j][k] % MOD);
                ans.mat[i][k] = ans.mat[i][k] % MOD;
            }
        }
    }
    return ans;
}

Matrix matPow(Matrix base, ll p) {
    Matrix ans;
    for (int i = 0; i < MAX_N; i++) {
        for (int j = 0; j < MAX_N; j++) ans.mat[i][j] = (i == j); //prepare identity matrix
    }
    while (p > 0) {
        if (p & 1) ans = matMul(ans,base); // check if p is odd
        base = matMul(base,base);
        p >>= 1;
    }
    return ans;
}

// use matrix exponentiation to find the pth number,denoted as F_{p} in O(log p)
// recursive relation is [1 1 1; 1 0 0; 0 0 1] * [F_{p} F_{p - 1} 1] = [F_{p + 1} F{p} 1]
int main() {
    ll N; scanf("%lld",&N);
    Matrix base;
    base = matPow(base, N - 1); // # need to multiply by N - 1 times
    //printf("res[1][0] = %lld, res[1][1] = %lld, res[1][2] = %lld\n", base.mat[1][0], base.mat[1][1], base.mat[1][2]);
    printf("%lld\n", ((base.mat[1][0] * 2) % MOD + (base.mat[1][1] + base.mat[1][2]) % MOD) % MOD);
    return 0;
}