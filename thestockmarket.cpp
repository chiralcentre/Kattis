#include <bits/stdc++.h>

using namespace std;

int n,k;

int main() {
    scanf("%d\n%d",&n,&k);
    vector<int> prices(n,0);
    for (int i = 0; i < n; i++) scanf("%d",&prices[i]);
    int best = -1e9;
    for (int i = 0; i < n - k; i++) best = max(best, prices[i + k] - prices[i]);
    printf("%d\n",best);
    return 0;
}