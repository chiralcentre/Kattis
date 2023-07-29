#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int T; string S;
ll MOD = 1000000007;
ll dp[2001][2001];


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> T;
    while (T--) {
        cin >> S;
        int N = S.length();
        memset(dp, 0, sizeof(dp)); // initialise dp table with zeroes
        // Case 1: Every single character is a palindrome
        for (int i = 0; i < N; i++) dp[i][i] = 1;
        // Case 2: S[i] == S[j] indicates this can be a palindromic subsequence, check for rest of subsequences
        // Case 3: check for rest of subsequences and remove common palindromic subsequences that are counted twice
        for (int i = N - 1; i >= 0; i--) {
            for (int j = i + 1; j < N; j++) {
                dp[i][j] = (S[i] == S[j]) ? (1 + dp[i + 1][j] + dp[i][j - 1]) % MOD: (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + MOD) % MOD;            
            }
        }
        cout << dp[0][N - 1] << "\n";
    }
    return 0;
}