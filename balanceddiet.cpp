#include <bits/stdc++.h>

using namespace std;

int cans[20], dp[20][12001], total = 0;

int findMinDiff(int i, int subsetSum) {
    if (i < 0) return abs(total - 2 * subsetSum);
    if (dp[i][subsetSum] != -1) return dp[i][subsetSum];
    dp[i][subsetSum] = min(findMinDiff(i - 1, subsetSum + cans[i]), findMinDiff(i - 1, subsetSum));
    return dp[i][subsetSum];
}

int main() {
    int N;
    while (true) {
        scanf("%d",&N);
        if (N == 0) break;
        total = 0;
        for (int i = 0; i < N; i++) {
            scanf("%d",&cans[i]);
            total += cans[i];
        }
        //set default state as -1
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < total + 1; j++) dp[i][j] = -1;
        }
        int minDiff = findMinDiff(N - 1, 0);
        printf("%d %d\n", (total + minDiff) >> 1, (total - minDiff) >> 1);
    }
    return 0;
}