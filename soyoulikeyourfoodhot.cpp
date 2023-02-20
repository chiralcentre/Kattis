#include <bits/stdc++.h>

using namespace std;

int main() {
    int a1,b1,a2,b2,a3,b3;
    scanf("%d.%d",&a1,&b1);
    scanf("%d.%d",&a2,&b2);
    scanf("%d.%d",&a3,&b3);
    int pt = 100 * a1 + b1;
    int p1 = 100 * a2 + b2;
    int p2 = 100 * a3 + b3;
    bool found = false;
    for (int i = 0; i <= pt / p1; i++) {
        int r = pt - i * p1;
        if (r % p2 == 0) {
            found = true;
            printf("%d %d\n",i, r / p2);
        }
    }
    if (!found) printf("none\n");
    return 0;
}