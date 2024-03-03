#include <bits/stdc++.h>

using namespace std;

int n,a,b,w;

int main() {
    scanf("%d %d %d",&n,&a,&b);
    int seen[2] = {0,0};
    for (int i = 0; i < n - 1; i++) {
        scanf("%d",&w);
        if (w == a) seen[0] = 1;
        if (w == b) seen[1] = 1;
    }
    int t = seen[0] + seen[1];
    if (seen[0] + seen[1] == 0) printf("-1\n");
    else if (seen[0] + seen[1] == 2) {
        for (int i = a; i <= b; i++) printf("%d\n",i);
    } else printf("%d\n", (seen[0] == 1) ? b: a);
    return 0;
}