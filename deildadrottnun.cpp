#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n;

int main() {
    scanf("%lld",&n);
    // allocate the money in the sequence 1,2,3...M s.t M(M + 1)/2 <= n
    // use quadratic formula
    ll m = floor((-1 + sqrt(1 + 8 * n)) / 2);
    ll L = n - ((m * (m + 1)) >> 1);
    // if there is any leftever, add 1 to the last L numbers, L <= M
    printf("%lld\n",m);
    for (int i = 0; i < m; i++) {
        (i < m - L) ? printf("%d", i + 1) : printf("%d", i + 2);
        if (i < m - 1) printf(" ");
    }
    printf("\n");
    return 0;
}