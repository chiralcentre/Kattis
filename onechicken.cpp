#include <bits/stdc++.h>

using namespace std;

int main() {
    int N,M; scanf("%d %d", &N, &M);
    if (M >= N) printf(M - N == 1 ? "Dr. Chaz will have 1 piece of chicken left over!\n" : "Dr. Chaz will have %d pieces of chicken left over!", M - N);
    else printf(N - M == 1 ? "Dr. Chaz needs 1 more piece of chicken!\n" : "Dr. Chaz needs %d more pieces of chicken!\n", N - M);
    return 0;
}