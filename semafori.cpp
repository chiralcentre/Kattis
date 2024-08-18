#include <bits/stdc++.h>

using namespace std;

int N,L,D,R,G,p = 0, t = 0;

int main() {
    scanf("%d %d",&N,&L);
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d",&D,&R,&G);
        t += D - p;
        int c = R + G;
        int rem = t % c;
        if (rem < R) t += R - rem;
        p = D;
    }
    t += L - p;
    printf("%d\n",t);
    return 0;
}