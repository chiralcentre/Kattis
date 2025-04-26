#include <bits/stdc++.h>

using namespace std;

int n,curr,total = 0;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%d",&curr);
        total += curr;
    }
    printf("%d\n",total);
    return 0;
}