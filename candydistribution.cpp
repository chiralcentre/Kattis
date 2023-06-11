#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll extEuclid(ll a, ll b, ll &x, ll &y) {// ax + by = gcd(a,b)
    ll xx = y = 0;
    ll yy = x = 1;
    while (b) {
        ll q = a / b;
        ll t = b; b = a % b; a = t;
        t = xx; xx = x - q * xx; x = t;
        t = yy; yy = y - q * yy; y = y;
    }
    return a; // return gcd(a,b)
}

ll modInverse(ll b, ll m) { // return b ^ (-1) mod m
    ll x,y;
    ll d = extEuclid(b,m,x,y); // pass x and y by reference
    if (d != 1) return -1; // use -1 to indicate failure
    return ((x % m) + m) % m;
}

int main() {
    int t; scanf("%d",&t);
    // find the number B such that (C * B - 1) % K = 0
    // (B * C) % K = 1 -> B is modular multiplicative inverse of C with respect to modulus K
    while (t--) {
        ll K,C; scanf("%lld %lld",&K,&C);
        // check if C and K are coprime
        // if not, modular multiplicative inverse with respect to modulus K does not exist
        // use extended euclidean algorithm to find modular multiplicative inverse
        // handle edge cases when K = 1 or C = 1
        if (K == 1) printf(C > 1 ? "1\n" : "2\n"); // two bags are needed when C = 1 and K = 1
        else if (C == 1) printf("%lld\n", K + 1); // when C = 1, K + 1 bags are needed
        else {
            ll ans = modInverse(C,K);
            printf(ans == -1 || ans > 1000000000 ? "IMPOSSIBLE\n" : "%lld\n", ans);
        }
    }
    return 0;
}