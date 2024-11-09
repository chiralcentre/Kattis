#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll MOD = 1e9 + 7;

ll choose2(ll n) {
    return (n * (n - 1)) >> 1;
}

int main() {
    ll n,m;
    scanf("%lld %lld",&n,&m);
    n %= MOD;
    m %= MOD;
    ll first = choose2(n) % MOD, second = choose2(m) % MOD;
    printf("%lld\n", (first * second) % MOD);
    return 0;
}