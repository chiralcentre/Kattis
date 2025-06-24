#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n,c,a,total = 0;

// The answer is impossible when the current queue length in minute i is never smaller than c * (n − i)
// total / c represents waiting time
int main() {
    scanf("%lld %lld",&n,&c);
    ll best = 1e18, ans = -1;
    for (ll i = 0; i < n; i++) {
        scanf("%lld",&a);
        total += a;
        if (total < c * (n - i) && total / c < best) {
            best = total / c;
            ans = i;
        }
        total = max(total - c, 0LL);
    }
    ans == -1 ? printf("impossible\n") : printf("%lld\n",ans);
    return 0;
}