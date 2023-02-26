#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

int main() {
    int n,m; scanf("%d %d",&n,&m);
    vi cans(n,0);
    for (int i = 0; i < n; i++) scanf("%d",&cans[i]);
    sort(cans.begin(), cans.end());
    vi::iterator lower;
    ll w = 0;
    for (int i = 0; i < m; i++) {
        int c; scanf("%d",&c);
        lower = lower_bound(cans.begin(),cans.end(),c);
        int L = lower - cans.begin();
        w += cans[L] - c;
    }
    printf("%lld\n",w);
    return 0;
}