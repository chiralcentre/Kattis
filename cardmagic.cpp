#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int M = 1000000009,N,K,T;

ll dp[101][5001];

ll solve(int index, int curr) {
    if (curr < 0) return 0;
    if (dp[index][curr] != -1) return dp[index][curr];
    if (index < N) {
        ll res = 0;
        for (int i = 1; i <= K; i++) res = (res + solve(index + 1, curr - i)) % M;
        dp[index][curr] = res;
    }
    return dp[index][curr];
}

int main() {
    scanf("%d %d %d",&N,&K,&T);
    memset(dp, -1, sizeof(dp));
    for (int i = 1; i < T + 1; i++) dp[N][i] = 0;
    dp[N][0] = 1;
    printf("%lld\n",solve(0,T));
    return 0;
}