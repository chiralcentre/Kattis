#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    ll n,m; scanf("%lld %lld",&n,&m);
    ll extra_edges = m - n + 1, extra = 0, vertices = 2, included = 2, ans = 1;
    while (extra < extra_edges) {
        ans += included;
        included += vertices;
        extra += vertices - 1;
        vertices++;
    }
    ll L = n - vertices;
    ans += (m + (m - L + 1)) * L / 2;
    printf("%lld\n",ans);
    return 0;
}