#include <bits/stdc++.h>

using namespace std;

int T,N,m;

int modExp(int x, int y, int p) {
    int ans = 1;
    while (y > 0) {
        if (y % 2 == 1) ans *= x;
        ans %= p;
        y >>= 1;
        x *= x;
        x %= p;
    }
    return ans % p;
}

int main() {
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&N);
        m = 0;
        while (N % 10 == 0) {
            N /= 10;
            m++;
        }
        printf("%d\n",--N * modExp(10,m,100000000));
    }
    return 0;
}