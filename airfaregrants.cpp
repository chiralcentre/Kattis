#include <bits/stdc++.h>

using namespace std;

int N,P,L = 1e9, H = -1;

int main() {
    scanf("%d",&N);
    for (int i = 0; i < N; i++) {
        scanf("%d",&P);
        L = min(L, P);
        H = max(H, P);
    }
    printf("%d\n", max(L - (H >> 1), 0));
    return 0;
}