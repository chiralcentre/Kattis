#include <bits/stdc++.h>

using namespace std;

int n,m,k,p,f[500001];

int main() {
    scanf("%d %d",&n,&m);
    for (int i = 0; i < n; i++) {
        scanf("%d",&k);
        for (int j = 0; j < k; j++) {
            scanf("%d",&p);
            f[p] = 1;
        }
    }
    for (int i = 1; i <= m; i++) {
        if (f[i] != 1) {
            printf("Neibb\n");
            return 0;
        }
    }
    printf("Jebb\n");
    return 0;
}