#include <bits/stdc++.h>

using namespace std;

int n,m,x,L = 1e9 + 1,H = -1;

int main() {
    scanf("%d %d",&n,&m);
    for (int i = 0; i < n; i++) {
        scanf("%d",&x);
        L = min(L, x);
        H = max(H, x);
        if (H - L > 1) {
            printf("ósvífinn kapítalisti\n");
            return 0;
        }
    }
    printf("da komrad\n");
    return 0;
}