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
        t = yy; yy = y - q * yy; y = t;
    }
    return a; // return gcd(a,b)
}

int main() {
    int T; scanf("%d", &T);
    while (T--) {
        ll a,b,d,x,y; scanf("%lld %lld %lld",&a,&b,&d);
        //Solve linear diophantine equation ax + by = d
        //d must be divisible by gcd(a,b) for equation to be solvable
        //use extended euclidean algorithm
        ll c = extEuclid(a,b,x,y);
        printf((d % c == 0) ? "Yes\n" : "No\n");
    }
    return 0;
}