#include <bits/stdc++.h>

using namespace std;

int n,k;

int main() {
    scanf("%d\n%d",&n,&k);
    if (k >= n) printf("impossible\n");
    else {
        for (int i = 1; i <= k; i++) {
            printf("open %d using %d\n",i,i + 1);
        }
    }
    return 0;
}