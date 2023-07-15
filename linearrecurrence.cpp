#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

int n,q; ll t,m;

ll mod(ll a, ll m) {
    return ((a % m) + m) % m; //ensure positive answer
}

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
        for (int j = 0; j < n; j++) {
            if (a.mat[i][j] == 0) continue; //optimisation
            for (int k = 0; k < n; k++) {
                ans.mat[i][k] += mod(a.mat[i][j], m) * mod(b.mat[j][k], m);
                ans.mat[i][k] = mod(ans.mat[i][k], m);
            }
        }
    }
    return ans;
}

Matrix matPow(Matrix base, ll p) {
    Matrix ans(n);
    for (int i = 0; i < n; i++) ans.mat[i][i] = 1; //prepare identity matrix
    while (p > 0) {
        if (p & 1) ans = matMul(ans,base); // check if p is odd
        base = matMul(base,base);
        p >>= 1;
    }
    return ans;
}

int main() {
    scanf("%d", &n);
    n++;
    Matrix base(n); vll x(n, 1);
    // take in values of a and store in second row of base matrix
    for (int i = 0; i < n; i++) scanf("%lld",&base.mat[1][i]);
    base.mat[0][0] = 1;
    // initialise rest of values in matrix
    for (int i = 2; i < n; i++) base.mat[i][i - 1] = 1;
    // take in initial values for recursion
    for (int i = 1; i < n; i++) scanf("%lld",&x[n - i]);
    scanf("%d",&q);
    while (q--) {
        scanf("%lld %lld",&t,&m);
        ll ans = 0;
        if (t < n - 1) {
            ans = mod(x[n - t - 1], m);
        } else {
            Matrix immd = matPow(base, t - n + 2);
            /*
            printf("immd: \n");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) printf("%lld ", immd.mat[i][j]);
                printf("\n");
            }
            printf("\n"); */
            for (int i = 0; i < n; i++) {
                ll prod = mod(mod(immd.mat[1][i], m) * mod(x[i], m), m);
                ans += prod;
                ans = mod(ans, m);
            }
        }
        printf("%lld\n", ans);
    }
    return 0;
}