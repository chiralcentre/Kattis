#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll MOD = 1000000000;

struct Matrix {ll mat[2][2];};

Matrix matMul (Matrix a, Matrix b) {
    Matrix ans;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) ans.mat[i][j] = 0;
    }
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            if (a.mat[i][j] == 0) continue; //optimisation
            for (int k = 0; k < 2; k++) {
                ans.mat[i][k] += (a.mat[i][j] % MOD) * (b.mat[j][k] % MOD);
                ans.mat[i][k] %= MOD;
            }
        }
    }
    return ans;
}

Matrix matPow(Matrix base, ll p) {
    Matrix ans;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) ans.mat[i][j] = (i == j); //prepare identity matrix
    }
    while (p > 0) {
        if (p & 1) ans = matMul(ans,base); // check if p is odd
        base = matMul(base,base);
        p >>= 1;
    }
    return ans;
}

// use matrix exponentiation to find the pth fibonacci number in O(log p)
int main() {
    int P; scanf("%d",&P);
    Matrix base;
    base.mat[0][0] = 1, base.mat[0][1] = 1; base.mat[1][0] = 1, base.mat[1][1] = 0;
    while (P--) {
        ll K,Y; scanf("%lld %lld",&K,&Y);
        printf("%lld %lld\n",K,matPow(base,Y).mat[0][1]);
    }
    return 0;
}