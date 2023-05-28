#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unordered_map<ll,ll> umll;

ll n,m;

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

bool solve(umll &pfM, ll m, ll n) {
    if (m == 0) return false; // edge case
    if (m <= n) return true;
    // use legendre's formula
    for (auto &[k,v]: pfM) {
        ll t = 0;
        for (ll p = k; p <= n; p *= k) t += n / p;
        if (t < v) return false;
    }
    return true;
}

int main() {
    while (scanf("%lld %lld",&n,&m) == 2) {
        umll pfM = primeFactor(m);
        printf("%lld %s %lld!\n", m, solve(pfM,m,n) ? "divides" : "does not divide", n);
    }
    return 0;
}