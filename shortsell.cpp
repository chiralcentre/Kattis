#include <bits/stdc++.h>

using namespace std;

int N,K,p;

int main() {
    scanf("%d %d",&N,&K);
    int ans = 0, best = 0;
    for (int i = 0; i < N; i++) {
        scanf("%d",&p);
        // this line allows for restart at current price
        best = max(best, 100 * p);
        best -= K;
        best = max(best, 0);
        ans = max(ans, best - p * 100);
    }
    printf("%d\n",ans);
    return 0;
}