#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

unordered_map<ll, ll> memo;

// OEIS A0006046
// A(2k) = 3 * A(k), A(2k + 1) = 2 * A(k) + A(k + 1)
ll solve(ll n) {
    if (memo.find(n) != memo.end()) return memo[n];
    memo[n] = (n % 2 == 1) ? 2 * solve(n / 2) + solve(n / 2 + 1) : 3 * solve(n / 2);
    return memo[n];
}

int main() {
    memo[0] = 0, memo[1] = 1;
    ll n; scanf("%lld",&n);
    printf("%lld\n",solve(n));
    return 0;
}