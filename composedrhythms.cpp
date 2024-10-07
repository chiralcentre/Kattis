#include <bits/stdc++.h>

using namespace std;

int N;

int main() {
    scanf("%d",&N);
    int rem = N % 3, q = N / 3;
    if (rem == 1) {
        printf("%d\n",q + 1);
        printf("2 2");
        for (int i = 0; i < q - 1; i++) printf(" 3");
    } else if (rem == 2) {
        printf("%d\n",q + 1);
        printf("2");
        for (int i = 0; i < q; i++) printf(" 3");
    } else {
        printf("%d\n",q);
        for (int i = 0; i < q; i++) {
            printf("3");
            if (i < q - 1) printf(" ");
        }
    }
    printf("\n");
    return 0;
}