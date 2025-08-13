#include <bits/stdc++.h>

using namespace std;

int N,a,t = 0;

int main() {
    scanf("%d",&N);
    scanf("%d",&a);
    t += a;
    for (int i = 1; i < N; i++) {
        scanf("%d",&a);
        if (a > 0) t += a - 1;
    }
    printf("%d\n",t);
    return 0;
}