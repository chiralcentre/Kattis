#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a / gcd (a , b) * b; }

int main() {
    int T; scanf("%d", &T);
    ll earliest = 12021; // 2021 + 100 * 100
    while (T--) {
        ll y,a,b; scanf("%lld %lld %lld",&y,&a,&b);
        ll t = lcm(a,b);
        earliest = min(y + t, earliest);
    }
    printf("%lld\n",earliest);
    return 0;
}