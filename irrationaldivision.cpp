#include <bits/stdc++.h>

using namespace std;

int main() {
    int p,q; scanf("%d %d",&p,&q);
    if (p % 2 == 1 && q % 2 == 1) printf("1\n");
    else if (p % 2 == 0) printf("0\n");
    else if (p < q) printf("2\n");
    else printf("0\n");
    return 0;
}