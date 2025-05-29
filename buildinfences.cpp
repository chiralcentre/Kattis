#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int N; ll x,y,xmin,xmax,ymin,ymax;

int main() {
    scanf("%d",&N);
    scanf("%lld %lld",&x,&y);
    xmin = x; xmax = x; ymin = y; ymax = y;
    for (int i = 0; i < N - 1; i++) {
        scanf("%lld %lld",&x,&y);
        xmin = min(x, xmin); xmax = max(x, xmax);
        ymin = min(y, ymin); ymax = max(y, ymax);
    }
    printf("%lld\n", (xmax - xmin + 2) * 2 + (ymax - ymin + 2) * 2);
    return 0;
}