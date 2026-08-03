#include <bits/stdc++.h>

using namespace std;

int M = 0, a = 0;

int main() {
    while (scanf("%d",&a) == 1) {
        M = max(M, a);
    }
    printf("%d\n",M);
    return 0;
}