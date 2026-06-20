#include <bits/stdc++.h>

using namespace std;

int n,k,x;

int main() {
    scanf("%d %d",&n,&k);
    unordered_map<int,int> freq;
    for (int i = 0; i < n; i++) {
        scanf("%d",&x);
        freq[x]++;
    }
    int ans = 0;
    for (const auto&[key,value]: freq) ans += min(value,k);
    printf("%d\n",ans);
    return 0;
}