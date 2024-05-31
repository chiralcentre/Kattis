#include <bits/stdc++.h>

using namespace std;

int k,q,a,b,solved[100001],best = 100001;

int main() {
    scanf("%d %d",&k,&q);
    for (int i = 0; i < q; i++) {
        scanf("%d %d",&a,&b);
        solved[b]++;
    }
    for (int i = 1; i <= k; i++) best = min(best, solved[i]);
    printf("%d\n",best);
    return 0;
}