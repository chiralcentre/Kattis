#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll extEuclid(ll a, ll b, ll &x, ll &y) {    // pass x and y by ref
    ll xx = y = 0;
    ll yy = x = 1;
    while (b) {                                    // repeats until b == 0
        ll q = a / b;
        tie(a, b) = tuple(b, a%b);
        tie(x, xx) = tuple(xx, x-q*xx);
        tie(y, yy) = tuple(yy, y-q*yy);
    }
    return a;                                      // returns gcd(a, b)
}
int main() {
    int T; scanf("%d", &T);
    while (T--) {
        ll R,S,Q,x,y; scanf("%lld %lld %lld",&R,&S,&Q);
        //Solve linear diophantine equation A*R + B*S = Q
        //Q must be divisible by d = gcd(R,S) for equation to be solvable
        //use extended euclidean algorithm
        ll d = extEuclid(R,S,x,y); 
        if (d < 0) {x = -x; y = -y; d = -d;} // negate signs when gcd is calculated as negative
        //multiply LHS and RHS by Q/d
        x *= (Q / d), y *= (Q / d);
        //solutions to A and B are A = x + (S / d) * n, B = y - (R / d) * n, where n is an integer
        //B > 0 -> y > (R / d) * n 
        //R >= 2 > 0 -> d * y / R > n
        //A > 0 -> x + (S / d) * n > 0 -> x > -(S / d) * n -> - x * d / S > n (since S <= -2 < 0)
        //combining two inequalities, n < min(d * y / R, -x * d / S)
        ll n1 = (d * y) % R != 0 ? floor(double(d) * double(y) / double(R)) : d * y / R - 1;
        ll n2 = (-x * d) % S != 0 ? floor(-double(x) * double(d) / double(S)) : -x * d / S - 1;
        ll n = min(n1,n2);
        printf("%lld %lld\n", x + (S / d) * n, y - (R / d) * n);
    } 
    return 0;
}