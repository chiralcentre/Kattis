#include <bits/stdc++.h>

using namespace std;

int n;

int main() {
    scanf("%d",&n);
    vector<int> prices(n, 0);
    for (int i = 0; i < n; i++) scanf("%d",&prices[i]);
    sort(prices.begin(),prices.end());
    printf("%d\n", prices[n - 2]);
    return 0;
}