#include <bits/stdc++.h>

typedef long long ll;

int main() {
    ll n, ans = 1; scanf("%lld",&n);
    // find power of 5, note that power of 2 must be more than power of 5 in n!
    ll f = 0;
    for (ll p = 5; p <= n; p *= 5) f += n / p;
    ll t = f; // note that t = f = min(a,b), where a is power of 2 and b is power of 5 in n! respectively
    for (ll i = 2; i <= n; i++) {
        ll z = i;
        // get rid of f copies of 2 and 5, thus removing trailing zeroes
        while (z % 2 == 0 && t-- > 0) z /= 2; 
        while (z % 5 == 0 && f-- > 0) z /= 5;
        ans *= z;
        ans %= 1000;
    }
    printf(n > 6 ? "%03lld\n" : "%lld\n", ans);
    return 0;
}