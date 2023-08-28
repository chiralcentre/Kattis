#include <bits/stdc++.h>

using namespace std;

int n,m,u;

int main() {
    scanf("%d %d",&n,&m);
    vector<int> ans(n,0);
    for (int i = 0; i < n; i++) ans[i] = i;
    for (int i = 0; i < m; i++) {
        scanf("%d",&u);
        swap(ans[u - 1],ans[u]);
    }
    for (int p: ans) printf("%d\n",p + 1);
    return 0;
}