#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll solve(ll x1, ll y1, ll x2, ll y2) {
    ll d1 = abs(x2 - x1), d2 = abs(y2 - y1);
    ll r = abs(d2 - d1), base = 2 * min(d1,d2);
    base += (r % 2 == 0) ? r / 2 * 4 : r / 2 * 4 + 1;
    return base;
}

int main() {
    int T; scanf("%d",&T);
    while (T--) {
        ll x1,y1,x2,y2; scanf("%lld %lld %lld %lld",&x1,&y1,&x2,&y2);
        printf("%lld\n",solve(x1,y1,x2,y2));
    }
    return 0;
}