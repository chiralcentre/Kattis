#include <bits/stdc++.h>

using namespace std;

int main() {
    int S; scanf("%d",&S);
    printf("%d:\n",S);
    for (int i = 2; i <= S/2 + 1; i++) {
        int m1 = S / (2 * i - 1);
        if ((m1 * (2 * i - 1) == S) || (m1 * (2 * i - 1) + i == S)) printf("%d,%d\n",i,i-1);
        int m2 = S / (2 * i);
        if ((m2 * (2 * i) == S) || (m2 * (2 * i) + i == S)) printf("%d,%d\n",i,i);
    }
    return 0;
}