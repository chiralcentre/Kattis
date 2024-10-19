#include <bits/stdc++.h>

using namespace std;

int N;

int main() {
    scanf("%d",&N);
    // use mathematical formula
    printf("%d\n", (N * (N + 1)) >> 1);
    printf("%d\n", (N * (N + 1) * (2 * N + 1) + 3 * N * (N + 1)) / 12);
    return 0;
}