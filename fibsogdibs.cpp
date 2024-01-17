#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll MOD = 1000000007;

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

// use matrix exponentiation to find the nth fibonacci number in O(log n)
int main() {
    ll a,b,n; scanf("%lld %lld\n%lld",&a,&b,&n);
    Matrix base;
    base.mat[0][0] = 1, base.mat[0][1] = 1; base.mat[1][0] = 1, base.mat[1][1] = 0;
    Matrix res = matPow(base, n << 1);
    // printf("%lld %lld\n%lld %lld\n", res.mat[0][0],res.mat[0][1],res.mat[1][0],res.mat[1][1]);
    ll elvar = ((res.mat[0][0] * b) % MOD + (res.mat[0][1] * a) % MOD) % MOD;
    ll dagur = ((res.mat[1][0] * b) % MOD + (res.mat[1][1] * a) % MOD) % MOD;
    printf("%lld %lld\n", dagur, elvar);
    return 0;
}