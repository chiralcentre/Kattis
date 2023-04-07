#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

//O(n) approach
int main() {
    int n,m; scanf("%d %d",&n,&m);
    vi arr(n,0);
    for (int i = 0; i < n; i++) scanf("%d",&arr[i]);
    int ans = 0, even = 0;
    for (int i = 0; i < m; i++) {
        if (arr[i] % 2 == 0) even++;
    }
    if (even >= 2) ans++;
    for (int i = m; i < n; i++) {
        if (arr[i - m] % 2 == 0) even--;
        if (arr[i] % 2 == 0) even++;
        if (even >= 2) ans++;
    }
    printf("%d\n",ans);
    return 0;
}