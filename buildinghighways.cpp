#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

// the city with smallest cost will form MST with other cities
int main() {
    ll N; scanf("%lld",&N);
    ll total = 0, lowest = 1e9;
    for (ll i = 0; i < N; i++) {
        ll t; scanf("%lld", &t);
        total += t;
        lowest = min(t,lowest);
    }
    printf("%lld\n", total + (N - 2) * lowest);
    return 0;
}