#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

ll p[3000], dp[3000];

int main() {
    int n; scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%lld",&p[i]);
        dp[i] = -1e18; //initialise to negative infinity
    }
    dp[0] = p[0];
    // go through all possible jump length s
    // O(n^2)
    for (int s = n - 1; s > 0; s--) {
        for (int i = s; i < n; i++) dp[i] = max(dp[i], p[i] + dp[i - s]);
    }
    printf("%lld\n",dp[n - 1]);
    return 0;
}