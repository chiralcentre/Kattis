#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int lst[1000001], primeFactors[1000001];
int MOD = 1000000007;

void initialise(int size) {
    for (int i = 0; i < size; i++) {
        lst[i] = i;
        primeFactors[i] = 0;
    }
}
void FactorSieve(int size) {
    for (int i = 3; i <= size; i += 2) {
        if (i * i > size) break;
        if (lst[i] == i) {
            for (int j = i * i; j <= size; j += 2 * i) lst[j] = i;
        }
    }
}

void primeFactorise(int n) {
    while (n % 2 == 0) {
        primeFactors[2]++;
        n /= 2;
    }
    while (n > 1) {
        int f = lst[n];
        while (n % f == 0) {
            primeFactors[f]++;
            n /= f;
        }
    }
}


int main() {
    int n; scanf("%d",&n);
    initialise(1000001);
    FactorSieve(1000001);
    for (int i = 0; i < n; i++) {
        int m; scanf("%d",&m);
        primeFactorise(m);
    }
    ll prod = 1;
    for (int k : primeFactors) {
        if (k > 0) {
            prod *= k + 1;
            prod %= MOD;
        }
    }
    printf("%lld\n", prod);
    return 0;
}