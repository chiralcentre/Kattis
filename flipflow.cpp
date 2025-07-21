#include <bits/stdc++.h>

using namespace std;

int t,s,n,a = 0,p = 0;

int main() {
    scanf("%d %d %d",&t,&s,&n);
    int lower = s, upper = 0;
    for (int i = 0; i < n; i++) {
        p = a;
        scanf("%d",&a);
        int r = max(0,min(upper, a - p));
        upper -= r;
        lower += r;
        swap(lower, upper);
    }
    printf("%d\n", max(0, a + upper - t));
    return 0;
}