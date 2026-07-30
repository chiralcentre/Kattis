#include <bits/stdc++.h>

using namespace std;

int T;

int main() {
    scanf("%d",&T);
    // Let n be the duration of last lap. Total time taken is n(n + 1) / 2.
    // n(n + 1) / 2 <= T -> n^2 + n - 2 * T <= 0 -> D = 1 + 8T, n >= (-1 - sqrt(D)) / 2 or n <= (-1 + sqrt(D)) / 2
    printf("%d\n", (int)((-1 + sqrt(1 + T << 3)) / 2));
    return 0;
}