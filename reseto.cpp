#include <bits/stdc++.h>

using namespace std;

bool sieve[100001];

int solve(int N, int K) {
    int p = 2, c = 0;
    while (p * p <= N) {
        if (sieve[p]) {
            for (int i = p; i <= N; i += p) {
                if (sieve[i]) c++;
                sieve[i] = false;
                if (c == K) return i;
            }
        }
        p++;
    }
}

int main() {
    int N,K; scanf("%d %d",&N,&K);
    for (int i = 0; i <= N; i++) sieve[i] = true;
    printf("%d\n",solve(N,K));
    return 0;
}