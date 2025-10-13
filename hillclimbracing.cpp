#include <bits/stdc++.h>

using namespace std;

int l,a,pre,curr;

int main() {
    scanf("%d %d",&l,&a);
    scanf("%d",&pre);
    for (int i = 0; i < l; i++) {
        scanf("%d",&curr);
        if (curr - pre > a) {
            printf("BUG REPORT\n");
            return 0;
        }
        pre = curr;
    }
    printf("POSSIBLE\n");
    return 0;
}