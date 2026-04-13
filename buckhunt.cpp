#include <bits/stdc++.h>

using namespace std;

int xa,xb,ya,yb,n,x,y;

int main() {
    scanf("%d %d %d %d",&xa,&xb,&ya,&yb);
    scanf("%d",&n);
    int ans = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d %d",&x,&y);
        if (xa <= x && x <= xb && ya <= y && y <= yb) ans++;
    }
    printf("%d\n",ans);
    return 0;
}