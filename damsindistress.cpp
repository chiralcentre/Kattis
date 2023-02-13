#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

int main() {
    int n; ll w; scanf("%d %lld",&n,&w);
    //requires w units of water at base camp
    vll dp(n + 1,w);
    for (int i = 1; i < n + 1; i++) {
        //c - u is required to break the current dam
        //d is downstream of i, and dp[d] - c needs to be added if dp[d] > c, since this means d has a larger capacity than i
        int d; ll c,u; scanf("%d %lld %lld",&d,&c,&u);
        dp[i] = c - u + max(0LL, dp[d] - c);
    }
    printf("%lld\n",*min_element(dp.begin(),dp.end()));
    return 0;
}