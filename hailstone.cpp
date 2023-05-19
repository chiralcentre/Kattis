#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll sum = 0;

void solve(ll n) {
    sum += n;
    if (n == 1) return;
    (n % 2) ? solve(3 * n + 1) : solve(n / 2);
}

int main() {
    ll n; scanf("%lld",&n);
    solve(n);
    printf("%lld\n",sum);
    return 0;
}