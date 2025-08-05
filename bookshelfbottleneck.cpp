#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n,H,l,w,h;

int main() {
    scanf("%lld %lld",&n,&H);
    ll ans = 0;
    for (int i = 0; i < n; i++){
        scanf("%lld %lld %lld",&l,&w,&h);
        vector<ll> edges = {l,w,h};
        sort(edges.begin(),edges.end());
        if (edges[1] <= H) ans += edges[0]; // use second edge as height
        else if (edges[0] <= H) ans += edges[1]; // use first edge as height
        else {
            printf("impossible\n");
            return 0;
        }
    }
    printf("%lld\n",ans);
    return 0;
}