#include <bits/stdc++.h>

using namespace std;

int n,t,a;

int main() {
    scanf("%d",&n);
    int total = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d %d",&t,&a);
        if (t == 0) total += a;
        else total = max(0,total - a);
    }
    printf("%d\n",total);
    return 0;
}