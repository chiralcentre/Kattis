#include <bits/stdc++.h>

using namespace std;

int r,g,b,cr,cg,cb,rg,gb;

int main() {
    scanf("%d %d %d\n%d %d %d\n%d %d",&r,&g,&b,&cr,&cg,&cb,&rg,&gb);
    int x = max(r - cr, 0), y = max(g - cg, 0), z = max(b - cb, 0);
    // use red green LEDs to fill red shortfall first, use green blue LEDs to fill blue shortfall first
    int rem_rg = rg - x, rem_gb = gb - z;
    if (rem_rg < 0 || rem_gb < 0) printf("-1\n");
    else {
        if (rem_rg + rem_gb < y) printf("-1\n");
        else printf("%d\n", x + y + z);
    }
    return 0;
}