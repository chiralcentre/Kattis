#include <bits/stdc++.h>

using namespace std;

int M,T,total = 0;

int main() {
    scanf("%d",&M);
    for (int i = 0; i < M; i++) {
        scanf("%d",&T);
        total += T;
    }
    printf("%d\n", total / M);
    return 0;
}