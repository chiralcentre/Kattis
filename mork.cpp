#include <bits/stdc++.h>

using namespace std;

int n,m;

int main() {
    scanf("%d\n%d",&n,&m);
    if (m == 0 || n == 0 || (n == 2 && m == 2)) printf("Jebb\n");
    else printf("Neibb\n");
    return 0;
}