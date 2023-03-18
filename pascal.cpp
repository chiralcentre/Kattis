#include <bits/stdc++.h>

using namespace std;

//perform factorisation in O(sqrt(N)) time to find largest factor
int main() {
    int N; scanf("%d",&N);
    int h = 1;
    for (int i = 2; i <= sqrt(N); i++) {
        if (N % i == 0) {h = N / i; break;}
    }
    printf("%d\n", N - h);
    return 0;
}