#include <bits/stdc++.h>

using namespace std;

int A,B,C,S,memo[21][21][21][21];

int dp(int a, int b, int c, int d) {
    if (memo[a][b][c][d] != -1) return memo[a][b][c][d];
    int ans = 1e9;
    // if d + 1 <= S, this means that one more book of width 1 can be placed on the current shelf
    if (a > 0) ans = (d + 1 <= S) ? min(ans, dp(a - 1, b, c, d + 1)): min(ans,1 + dp(a - 1, b, c, 1));
    if (b > 0) ans = (d + 2 <= S) ? min(ans, dp(a, b - 1, c, d + 2)): min(ans,1 + dp(a, b - 1, c, 2));
    if (c > 0) ans = (d + 3 <= S) ? min(ans, dp(a, b, c - 1, d + 3)): min(ans,1 + dp(a, b, c - 1, 3));
    memo[a][b][c][d] = ans;
    return ans;
}

int main() {
    memset(memo, -1, sizeof(memo)); // set default as -1
    memo[0][0][0][0] = 0;
    for (int i = 1; i <= 20; i++) memo[0][0][0][i] = 1;
    scanf("%d %d %d\n %d",&A,&B,&C,&S);
    printf("%d\n",dp(A,B,C,0));
    return 0;
}