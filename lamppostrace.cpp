#include <bits/stdc++.h>

using namespace std;

int N;

int main() {
    scanf("%d\n",&N);
    vector<int> lp(N, 0);
    for (int i = 0; i < N; i++) scanf("%d",&lp[i]);
    int ans = lp[0];
    for (int i = 0; i < N - 1; i++) ans += abs(lp[i] - lp[i + 1]);
    printf("%d\n",ans);
    return 0;
}