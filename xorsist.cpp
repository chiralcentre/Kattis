#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll n;

ll res(ll x) {
    ll ans[4] = {x, 1LL, x+1LL, 0LL};
    return ans[x%4];
}

int main() {
    scanf("%lld",&n);
    ll ans = res(n);
    if (ans == 0) printf("Enginn\n");
    else if (1 <= ans && ans <= n) printf("%lld\n",ans);
    else printf("Gunnar\n");
    return 0;
}