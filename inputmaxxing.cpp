#include <bits/stdc++.h>

using namespace std;

int n,ans,curr;

int main() {
    scanf("%d",&n);
    ans = n;
    for (int i = 0; i < n; i++) {
        scanf("%d", &curr);
        if (curr > ans) ans = curr;
    }
    printf("%d\n",ans);
    return 0;
}