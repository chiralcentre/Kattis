#include <bits/stdc++.h>

int memo[1000001], n;

// credits to https://math.stackexchange.com/questions/130352/last-non-zero-digit-of-a-factorial for solution
int D(int n) {
    if (memo[n] != -1) return memo[n];
    // check if tens digit of N is even or odd;
    int t = (n % 100) / 10, u = n % 10;
    memo[n] = (t % 2 == 1) ? 4 * D(n / 5) * D(u) : 6 * D(n / 5) * D(u);
    memo[n] %= 10;
    return memo[n];
}

int main() {
    memo[0] = 1, memo[1] = 1, memo[2] = 2, memo[3] = 6, memo[4] = 4;
    memo[5] = 2, memo[6] = 2, memo[7] = 4, memo[8] = 2, memo[9] = 8;
    for (int i = 10; i <= 1000000; i++) memo[i] = -1; // state = -1 means not computed
    scanf("%d",&n);
    while (n != 0) {
        printf("%d\n", D(n));
        scanf("%d",&n);
    }
    return 0;
}