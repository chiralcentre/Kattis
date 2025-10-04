#include <bits/stdc++.h>

using namespace std;

int N,K,A;

int main() {
    scanf("%d %d",&N,&K);
    for (int i = 0; i < N; i++) {
        scanf("%d",&A);
        if (A <= K) {
            K -= A;
            printf("1");
        } else {
            printf("0");
        }
    }
    printf("\n");
    return 0;
}