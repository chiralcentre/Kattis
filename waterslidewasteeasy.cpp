#include <bits/stdc++.h>

using namespace std;

int n,w,total = 0;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%d",&w);
        total += w;
    }
    printf("%d\n",total);
    return 0;
}