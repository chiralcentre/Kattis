#include <bits/stdc++.h>

using namespace std;

int i,l,w,h;

int main() {
    scanf("%d",&i);
    if (i == 1) {
        scanf("%d",&l);
        w = l;
        h = 3;
    } else if (i == 2) {
        scanf("%d\n%d",&l,&w);
        h = 3;
    } else {
        scanf("%d\n%d\n%d",&l,&w,&h);
    }
    printf("%d\n", l * w * h -  (h - 1) * (w - 2) * (l - 2));
    return 0;
}