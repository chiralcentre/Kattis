#include <bits/stdc++.h>

using namespace std;

int n,s,l,r;

int main() {
    scanf("%d %d",&n,&s);
    for (int i = 0; i < n; i++) {
        scanf("%d %d",&l,&r);
        if (l <= s && s <= r) s++;
    }
    printf("%d\n",s);
    return 0;
}