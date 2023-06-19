#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll modExp(ll x, ll y, ll p) {
    ll ans = 1;
    while (y > 0) {
        if (y % 2 == 1) ans *= x;
        ans %= p;
        y >>= 1;
        x *= x;
        x %= p;
    }
    return ans % p;
}

//note that for x from 0 to a - 1, x^b + (a - x)^b ≡ x^b + (-x)^b ≡ 0 (mod a)
//when a is even, sum evaluates to (a/2)^b, else 0
int main() {
    ll a,b; scanf("%lld %lld",&a,&b);
    printf(a % 2 == 1 ? "0\n": "%lld\n", modExp(a / 2, b, a));
    return 0;
}