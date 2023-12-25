#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n; char store[100];

int main() {
    scanf("%d",&n);
    vector<ll> prices(n,0);
    for (int i = 0; i < n; i++) {
        scanf("%s",store);
        scanf("%lld",&prices[i]);
    }
    sort(prices.begin(), prices.end());
    ll total = 0;
    for (int i = n - 1; i >= 0; i -= 2) total += prices[i];
    printf("%lld\n",total);
    return 0;
}