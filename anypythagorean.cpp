#include <bits/stdc++.h>

using namespace std;

int n;

int main() {
    scanf("%d",&n);
    for (int i = 1; i < n / 3; i++) {
        for (int j = i + 1; 2 * j + i < n; j++) {
            int r = n - i - j;
            if (i * i + j * j == r * r) {
                printf("%d %d %d\n",i,j,r);
                return 0;
            }
        }
    }
    printf("0 0 0\n");
    return 0;
}