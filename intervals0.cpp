#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int n,k,a,b;

int main() {
    scanf("%d %d",&n,&k);
    vi freq(24, 0);
    int ans = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d %d",&a,&b);
        for (int j = a; j < b; j++) {
            freq[j]++;
        }
    }
    for (int i = 0; i < 24; i++) {
        if (freq[i] >= k) ans++;
    }
    printf("%d\n",ans);
    return 0;
}