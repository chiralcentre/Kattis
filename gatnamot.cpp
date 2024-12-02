#include <bits/stdc++.h>

typedef long long ll;

ll r;

int main() {
    scanf("%lld",&r);
    // Gauss circle problem
    // number of points in each quadrant is the same
    ll p = 0;
    for (ll i = 0; i < r; i++) {
        ll rem = r * r - i * i;
        ll root = floor(sqrt(rem));
        p += root;
    }
    printf("%lld\n", (p << 2) + 1);
}