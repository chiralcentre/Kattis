#include <bits/stdc++.h>

using namespace std;

int xb,yb,x,y,n;

int main() {
    scanf("%d %d",&xb,&yb);
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d",&x,&y);
        if ((x - xb) * (x - xb) + (y - yb) * (y - yb) <= 64) {
            printf("NO\n");
            return 0;
        }
    }
    printf("YES\n");
    return 0;
}