#include <bits/stdc++.h>

using namespace std;

int g,r;

int main() {
    scanf("%d %d",&g,&r);
    int p = min(g, r);
    int ans = p * 10;
    g -= p; r -= p;
    ans += (g / 3) * 10;
    g %= 3;
    if (g == 2) ans += 3;
    else if (g == 1) ans++;
    printf("%d\n",ans);
    return 0;
}