#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    ll A,B; scanf("%lld %lld", &A, &B);
    // go through all factors of A, and find factor closest to B
    // runs in O(sqrt(N))
    ll d = 1000000000000000000;
    for (ll i = 1; i <= sqrt(A); i++) {
        if (A % i == 0) {
            ll other = A / i;
            if (abs(other - B) < d) d = abs(other - B);
            if (abs(i - B) < d) d = abs(i - B);
        }
    }
    printf("%lld\n",d);
    return 0;
}