#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vll;

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

int main() {
    ll a,n,b,m,K,t;
    scanf("%d",&t);
    for (int i = 0; i < t; i++) {
        scanf("%lld %lld %lld %lld",&a,&n,&b,&m);
        vll r{a,b}, md{n,m};
        K = n * m;
        printf("%lld %lld\n", crt(r,md), K);
    }
    return 0;
}