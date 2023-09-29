#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int N; ll V,l,w,h;

int main() {
    scanf("%d %lld",&N,&V);
    ll ans = -1;
    for (int i = 0; i < N; i++) {
        scanf("%lld %lld %lld",&l,&w,&h);
        ll t = l * w * h;
        ans = max(t,ans);
    }
    printf("%lld\n",ans - V);
    return 0;
}