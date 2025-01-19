#include <bits/stdc++.h>

int N,M;

int main() {
    scanf("%d\n%d",&N,&M);
    int moves = 0;
    // use DP if N <= 2 * (M - 1) else use greedy algorithm
    while (N > 0) {
        if (M <= N && N <= 2 * (M - 1)) {
            moves += 2; // two moves are sufficient
            break;
        }
        int rem = N % M;
        if (rem > 0) N -= rem;
        else N /= M;
        moves++;
    }
    printf("%d\n",moves);
    return 0;
}