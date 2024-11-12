#include <bits/stdc++.h>

using namespace std;

int N,a,b,L,R;

int main() {
    scanf("%d",&N);
    scanf("%d %d",&a,&b);
    L = a; R = b;
    for (int i = 1; i < N; i++) {
        scanf("%d %d",&a,&b);
        if (b < L || a > R) {
            printf("bad news\n");
            return 0;
        }
        L = max(a,L);
        R = min(b,R);
    }
    printf("%d %d\n", R - L + 1, L);
    return 0;
}