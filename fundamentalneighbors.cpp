#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unordered_map<ll,ll> umll;

ll n;

umll primeFactor(ll n) {
    umll pf;
    if (n == 0) return pf; // special case
    if (n % 2 == 0) pf[2] = 0;
    while (n % 2 == 0) {
        n /= 2;
        pf[2]++;
    }
    for (ll i = 3; i <= ll(sqrt(n)); i += 2) { // n must be odd now
        if (n % i == 0) pf[i] = 0;
        while (n % i == 0) {
            n /= i;
            pf[i]++;
        }
    }
    if (n > 2) pf[n] = 1; // if n is a prime number > 2
    return pf;
}

ll modExp(ll x, ll y, ll p) {
    ll ans = 1;
    while (y > 0) {
        if (y % 2 == 1) ans *= x;
        y >>= 1;
        x *= x;
    }
    return ans % p;
}
 
int main() {
    while (scanf("%lld",&n) == 1) {
        umll pf = primeFactor(n);
        ll ans = 1;
        for (auto &[k,v]: pf) ans *= modExp(v, k, 2147483648);
        printf("%lld %lld\n",n,ans);
    }
    return 0;
}