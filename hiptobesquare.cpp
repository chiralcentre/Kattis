#include <bits/stdc++.h>

using namespace std;

int T,N;

int main() {
    scanf("%d",&T);
    for (int i = 0; i < T; i++) {
        scanf("%d",&N);
        int s = sqrt(N + 1); // largest length of square 
        printf("%d\n", (s - 1) >> 1);
    }
    return 0;
}