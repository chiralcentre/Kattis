#include <bits/stdc++.h>

using namespace std;

typedef long double ld;
typedef long long ll;
typedef vector<ll> vll;

int n,m,k;

int main() {
    scanf("%d %d %d",&n,&m,&k);
    vll download_sizes(n, 0ll);
    ll total = 0, downloaded_max = 0;
    for (int i = 0; i < n; i++) {
        scanf("%lld",&download_sizes[i]);
        total += download_sizes[i];
    }
    sort(download_sizes.begin(),download_sizes.end(),greater<ll>());
    for (int i = 0; i < min(m + k, n); i++) downloaded_max += download_sizes[i];
    printf("%Lf\n", ld(downloaded_max) * 100 / ld(total));
    return 0;
}