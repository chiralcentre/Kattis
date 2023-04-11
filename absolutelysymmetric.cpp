#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

// check if entry A[i][j] and A[j][i] have the same parity for all i and j and if matrix is absolutely symmetric
int parityAbsolutelySymmetric(vvll &A, int n) {
    bool absolutelySymmetric = true;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (abs(A[i][j]) % 2 != abs(A[j][i]) % 2) return -1;
            if (abs(A[i][j]) != abs(A[j][i])) absolutelySymmetric = false;
        }
    }
    return absolutelySymmetric ? 1 : 0;
}

void printMatrix(vvll &A, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%lld",A[i][j]);
            if (j < n - 1) printf(" ");
        }
        printf("\n");
    }
}

int main() {
    int n; scanf("%d",&n);
    vvll A(n,vll(n,0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lld",&A[i][j]);
        }
    }
    int res = parityAbsolutelySymmetric(A,n);
    if (res == -1) printf("-1\n");
    else if (res == 1) {
        printf("1\n");
        printMatrix(A,n);
    } else { //every matrix can be decomposed into two absolutely symmetric matrices
        printf("2\n");
        vvll B(n,vll(n,0)); vvll C(n,vll(n,0));
        // Let x = A[i][j] and y = A[j][i]
        // Let a = (x + y) / 2, b = (x - y) / 2
        // a + b = x, a - b = y
        // Let B[i][j] = a, B[j][i] = a, C[i][j] = b, C[j][i] = -b;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                ll x = A[i][j], y = A[j][i];
                ll a = (x + y) >> 1, b = (x - y) >> 1;
                B[i][j] = B[j][i] = a;
                C[i][j] = b; C[j][i] = -b;
            }
        }
        printMatrix(B,n);
        printMatrix(C,n);
    }
    return 0;
}