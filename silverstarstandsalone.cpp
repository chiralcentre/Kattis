#include <bits/stdc++.h>

typedef long long ll;

int P, primes[47] = {
    2,3,5,7,11,13,17,19,23,29,
    31,37,41,43,47,53,59,61,67,71,
    73,79,83,89,97,101,103,107,109,113,
    127,131,137,139,149,151,157,163,167,173,
    179,181,191,193,197,199,211
};

ll dp[47] = {0};

int get_prime_index() {
    for (int i = 0; i < 47; i++) {
        if (primes[i] == P) return i;
    }
    return -1;
}

int main() {
    scanf("%d",&P);
    int p = get_prime_index();
    dp[0] = 1;
    for (int i = 0; i <= p; i++) {
        for (int j = i + 1; j <= p && primes[j] - primes[i] <= 14; j++) {
            dp[j] += dp[i];
        }
    }
    printf("%lld\n",dp[p]);
    return 0;
}
