#include <bits/stdc++.h>

using namespace std;

int n,m,t,T = 0;

int main() {
    scanf("%d %d",&n,&m);
    for (int i = 0; i < m; i++) {
        scanf("%d",&t);
        T += t;
    }
    printf("%d\n", (T % n == 0) ? 1 : 0);
    return 0;
}