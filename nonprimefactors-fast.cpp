#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int factors[2000001], pf[2000001], Q,n;

int exponent(int N, int P) {
    int ans = 0;
    while (N % P == 0) {
        ans++;
        N /= P;
    }
    return ans;
}

int main() {
    scanf("%d", &Q);
    //initialisation and precomputation
    for (int i = 0; i <= 2000000; i++) factors[i] = 1;
    for (int i = 0; i <= 2000000; i++) pf[i] = 0;
    for (int i = 2; i <= 2000000; i++) {
        if (pf[i] == 0) { // i is a prime factor
            for (int j = i * 2; j <= 2000000; j += i) {
                pf[j]++;
                factors[j] *= (1 + exponent(j,i));
            }
        }
    }
    while (Q--) {
        scanf("%d", &n);
        printf("%d\n", factors[n] - pf[n]);
    }
    return 0;
}