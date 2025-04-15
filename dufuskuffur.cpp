#include <bits/stdc++.h>

using namespace std;

int n,m;

int main() {
    scanf("%d\n%d",&n,&m);
    if (n < m) printf("Dufur passa\n");
    else if (n > m) printf("Dufur passa ekki\n");
    else printf("Dufur passa fullkomlega\n");
    return 0;
}