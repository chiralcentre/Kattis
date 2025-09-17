#include <bits/stdc++.h>

using namespace std;

int N,K,a;

int main() {
    scanf("%d %d",&N,&K);
    for (int i = 0; i < K; i++) {
        scanf("%d",&a);
        if (a - 1 <= N - a) printf("1");
        else printf("%d", N);
        if (i < K - 1) printf(" ");
    }
    return 0;
}