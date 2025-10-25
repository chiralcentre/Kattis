#include <bits/stdc++.h>

using namespace std;

int n,p,m,a,b;

int main() {
    scanf("%d\n%d\n%d",&n,&p,&m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d",&a,&b);
        if (p == a) p = b;
        else if (p == b) p = a;
    }
    printf("%d\n",p);
    return 0;
}