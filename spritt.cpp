#include <bits/stdc++.h>

using namespace std;

int n,x,a,t = 0;

int main() {
    scanf("%d %d",&n,&x);
    while (n--) {
        scanf("%d",&a);
        t += a;
    }
    (t > x) ? printf("Neibb\n") : printf("Jebb\n");
    return 0;
}