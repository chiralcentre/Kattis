#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vll;
typedef unordered_map<ll,ll> umll;

ll mod(ll a, ll m) {                           // returns a (mod m)
  return ((a % m) + m) % m;                        // ensure positive answer
}

ll extEuclid(ll a, ll b, ll &x, ll &y) {    // pass x and y by ref
  ll xx = y = 0;
  ll yy = x = 1;
  while (b != 0) {                                    // repeats until b == 0
    ll q = a/b;
    tie(a, b) = tuple(b, a%b);
    tie(x, xx) = tuple(xx, x-q*xx);
    tie(y, yy) = tuple(yy, y-q*yy);
  }
  return a;                                      // returns gcd(a, b)
}

ll modInverse(ll b, ll m) {                   // returns b^(-1) (mod m)
  ll x, y;
  ll d = extEuclid(b, m, x, y);                 // to get b*x + m*y == d
  if (d != 1) return -1;                         // to indicate failure
  // b*x + m*y == 1, now apply (mod m) to get b*x == 1 (mod m)
  return mod(x, m);
}

ll crt(vll &r, vll &m) {
  // m_t = m_0*m_1*...*m_{n-1}
  ll mt = 1;
  // do not use accumulate with multiplies
  for (ll elem: m) mt *= elem;
  ll x = 0;
  for (int i = 0; i < (int) m.size(); ++i) {
    ll a = mod(r[i] * modInverse(mt/m[i], m[i]), m[i]);
    x = mod(x + a * (mt/m[i]), mt);
  }
  return x;
}

umll PrimeFactor(ll n) {
    umll factors;
    while (n % 2 == 0){ 
        factors[2]++;
        n >>= 1;
    }
    for (ll i = 3; i < ll(sqrt(n)) + 1; i += 2) { 
        if (n < 2) break;
        while (n % i == 0) {
            factors[i]++;
            n /= i;
        }
    }
    if (n > 2) factors[n] = 1;
    return factors;
}

ll modExp(ll x, ll y) {
    ll ans = 1;
    while (y > 0) {
        if (y % 2 == 1) ans *= x;
        y >>= 1;
        x *= x;
    }
    return ans;
}


int main() {
    ll a,n,c,d,b,m,K,t;
    scanf("%d",&t);
    for (int i = 0; i < t; i++) {
        scanf("%lld %lld %lld %lld",&a,&n,&b,&m);
        // c,d are dummy variables
        K = extEuclid(n,m,c,d);
        if (a % K == b % K) {
            umll pf1 = PrimeFactor(n);
            umll pf2 = PrimeFactor(m);
            vll r,md;
            for (auto &[k,v]: pf1) {
                if (pf2.find(k) == pf2.end()) {
                    ll p = modExp(k,v);
                    r.push_back(a % p);
                    md.push_back(p);
                } else { // prime factor appears in both, take equation with higher power
                    ll p = modExp(k,max(v,pf2[k]));
                    if (pf2[k] > v) r.push_back(b % p);
                    else r.push_back(a % p);
                    md.push_back(p);
                }
            } 
            for (auto &[k,v]: pf2) {
                if (pf1.find(k) == pf1.end()) {
                    ll p = modExp(k,v);
                    r.push_back(b % p);
                    md.push_back(p);
                }
            }
            printf("%lld %lld\n", crt(r,md), n * m / K);
        } else printf("No solution\n");
    }
    return 0;
}