#include <bits/stdc++.h>

using namespace std;

int M,H = -1,L = 1e9,TH = -1,TL = 1e9,S,a;

int main() {
    scanf("%d",&M);
    for (int i = 0; i < M; i++) {
        scanf("%d",&S);
        int total = 0;
        for (int j = 0; j < S; j++) {
            scanf("%d",&a);
            L = min(a, L);
            H = max(a, H);
            total += a;
        }
        TH = max(TH, total);
        TL = min(TL, total);
    }
    printf("%d\n%d\n%d\n%d\n",H,L,TH,TL);
    return 0;
}