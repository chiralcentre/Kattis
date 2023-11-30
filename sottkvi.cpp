#include <bits/stdc++.h>

using namespace std;

int n,k,d,q,b,t = 0;

int main() {
    scanf("%d %d %d",&n,&k,&d);
    b = k + d;
    while (n--) {
        scanf("%d",&q);
        t += (q + 14 <= b);
    }
    printf("%d\n",t);
    return 0;
}