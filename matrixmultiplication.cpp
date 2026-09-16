#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

static inline int readInt() {
    static char buf[1 << 20];
    static int len = 0, pos = 0;
    auto gc = [&]() -> int {
        if (pos == len) {
            len = (int)fread(buf, 1, sizeof(buf), stdin);
            pos = 0;
            if (len == 0) return -1;
        }
        return buf[pos++];
    };
    int c = gc();
    while (c == ' ' || c == '\n' || c == '\r' || c == '\t') c = gc();
    int x = 0;
    while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = gc(); }
    return x;
}

int solve(int n, int x, int y, int m, vvll &A, vvll &B, vvll &C) {
    if (x != y) return 0;
    vll rv(m,0);
    for (int k = 0; k < 7; k++) {
        for (int i = 0; i < m; i++) rv[i] = rand() % 2;
        vll I(y,0), D(n,0);
        for (int i = 0; i < y; i++) {
            ll dot_product = 0;
            for (int j = 0; j < m; j++) dot_product += B[i][j] * rv[j];
            I[i] = dot_product;
        }
        for (int i = 0; i < n; i++) {
            ll dot_product = 0;
            for (int j = 0; j < y; j++) dot_product += A[i][j] * I[j];
            D[i] = dot_product;
        }
        for (int i = 0; i < n; i++) {
            ll dot_product = 0;
            for (int j = 0; j < m; j++) dot_product += C[i][j] * rv[j];
            if (dot_product != D[i]) return 1;
        }
    }
    return 2;
}

int main() {
    int TC = readInt();
    while (TC--) {
        int n = readInt(), x = readInt(), y = readInt(), m = readInt();
        vvll A(n,vll(x,0)), B(y,vll(m,0)), C(n,vll(m,0));
        for (int i = 0; i < n; i++) for (int j = 0; j < x; j++) A[i][j] = readInt();
        for (int i = 0; i < y; i++) for (int j = 0; j < m; j++) B[i][j] = readInt();
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) C[i][j] = readInt();
        int result = solve(n,x,y,m,A,B,C);
        (result == 0) ? printf("Inner matrix dimensions must agree\n") : ((result == 1) ? printf("WA\n"): printf("AC\n"));
    }
    return 0;
}