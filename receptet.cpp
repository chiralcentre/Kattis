#include <bits/stdc++.h>

using namespace std;

int N,H,B,K,ans;

int main() {
    scanf("%d",&N);
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d",&H,&B,&K);
        if (B > H) ans += (B - H) * K;
    }
    printf("%d\n",ans);
    return 0;
}