#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int N,Q; ll x,y,p;

int main() {
    scanf("%d",&N);
    vector<ll> dist;
    for (int i = 0; i < N; i++) {
        scanf("%lld %lld",&x,&y);
        ll d = ceil(sqrt(x * x + y * y));
        dist.push_back(d);
    }
    sort(dist.begin(), dist.end());
    scanf("%d",&Q);
    for (int i = 0; i < Q; i++) {
        scanf("%lld",&p);
        printf("%d\n",lower_bound(dist.begin(), dist.end(), p + 1) - dist.begin());
    }
    return 0;
}