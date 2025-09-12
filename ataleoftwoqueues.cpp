#include <bits/stdc++.h>

using namespace std;

int n,m,a,L = 0, R = 0;

int main() {
    scanf("%d %d",&n,&m);
    for (int i = 0; i < n; i++) {
        scanf("%d",&a);
        L += a;
    }
    for (int i = 0; i < m; i++) {
        scanf("%d",&a);
        R += a;
    }
    if (L < R) printf("left\n");
    else if (L > R) printf("right\n");
    else printf("either\n");
    return 0;
}