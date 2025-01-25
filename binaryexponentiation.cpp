#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


ll mulmod(ll a, ll b, ll mod) {
    ll res = 0; // Initialize result
    a %= mod;
    while (b > 0) {
        if (b % 2 == 1) res = (res + a) % mod;
        a = (a << 1) % mod;
        // Divide b by 2
        b >>= 1;
    }
    return res % mod;
}

ll modExp(ll x, ll y, ll p) {
    ll ans = 1;
    while (y > 0) {
        if (y % 2 == 1) ans = mulmod(ans, x, p);
        // ans %= p;
        y >>= 1;
        x = mulmod(x, x, p);
        // x %= p;
    }
    return ans % p;
}

ll a,e,m;

int main() {
    scanf("%lld %lld %lld",&a,&e,&m);
    printf("%lld\n",modExp(a,e,m));
    return 0;
}

