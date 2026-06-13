#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n;

int main() {
    scanf("%d",&n);
    vector<ll> h(n, 0ll);
    for (int i = 0; i < n; i++) scanf("%lld",&h[i]);
    int L = 0, R = n - 1;
    ll ans = 0;
    while (L < R) {
        ans = max(ans, (R - L) * (min(h[L],h[R])));
        (h[L] < h[R]) ? L++ : R--;
    }
    printf("%lld\n",ans);
    return 0;
}