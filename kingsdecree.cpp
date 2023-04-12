#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

int main() {
    int C; scanf("%d",&C); 
    while (C--) {
        int n; scanf("%d",&n);
        vll W(n,0), L(n,0); ll highest = 0;
        for (int i = 0; i < n; i++) {
            scanf("%lld",&W[i]);
            highest = max(highest,W[i]);
        }
        for (int i = 0; i < n; i++) scanf("%lld", &L[i]);
        // binary search on lambda
        // runs in O(n log h), where h is value of highest
        ll lambda = 0, s = 0, e = highest;
        while (s <= e) {
            ll m = s + ((e - s) >> 1);
            ll donated = 0, needed = 0;
            for (int i = 0; i < n; i++) {
                if (W[i] <= m) needed += m - W[i];
                else donated += max(0ll,W[i] - max(L[i], m));
            }
            if (needed <= donated) {
                lambda = m;
                s = m + 1;
            } else {
                e = m - 1;
            }
        }
        printf("%lld\n",lambda);
    }
    return 0;
}