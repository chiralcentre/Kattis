#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int MAX_N = 300001;
const ll p = 131, M = 1e18 + 7;                   // p and M are relatively prime

ll P[MAX_N];                                  // to store p^i % M
ll h[MAX_N];                                    // to store prefix hashes
string T;
int Q,L,R;

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
 
void computeRollingHash() {                      // Overall: O(n)
    P[0] = 1;                                    // compute p^i % M
    for (int i = 1; i < T.length(); ++i)                    // O(n)
        P[i] = mulmod(P[i - 1], p, M);
    h[0] = 0;
    for (int i = 0; i < T.length(); ++i) {                  // O(n)
        if (i != 0) h[i] = h[i-1];                   // rolling hash
        h[i] = (h[i] + mulmod(T[i], P[i], M)) % M;
    }
}

ll extEuclid(ll a, ll b, ll &x, ll &y) {    // pass x and y by ref
    ll xx = y = 0;
    ll yy = x = 1;
    while (b) {                                    // repeats until b == 0
        ll q = a / b;
        tie(a, b) = tuple(b, a % b);
        tie(x, xx) = tuple(xx, x - q * xx);
        tie(y, yy) = tuple(yy, y - q * yy);
    }
    return a;                                      // returns gcd(a, b)
}

ll modInverse(ll b, ll m) {                   // returns b^(-1) (mod m)
    ll x, y;
    ll d = extEuclid(b, m, x, y);                 // to get b*x + m*y == d
    if (d != 1) return -1;                         // to indicate failure
    // b*x + m*y == 1, now apply (mod m) to get b*x == 1 (mod m)
    return (x + m) % m;                                // this is the answer
}

ll hash_fast(int L, int R) {                    // O(1) hash of any substr
    if (L == 0) return h[R];                       // h is the prefix hashes
    ll ans = 0;
    ans = ((h[R] - h[L-1]) % M + M) % M;           // compute differences
    ans = mulmod(ans,modInverse(P[L], M),M);   // remove P[L]^-1 (mod M)
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> T >> Q;
    computeRollingHash();
    for (int i = 0; i < Q; i++) {
        cin >> L >> R;
        cout << hash_fast(L, R - 1) << "\n";
    }
    return 0;
}


