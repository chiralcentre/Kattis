#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int memo[1001][1001], V[1001], W[1001];
int L,n;

//bottom up DP
int dp(int id, int remW) {
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= L; w++) {
            if (i == 0 || w == 0) memo[i][w] = 0;
            else if (W[i - 1] <= w) memo[i][w] = max(V[i - 1] + memo[i - 1][w - W[i - 1]], memo[i - 1][w]); //choose one item
            else memo[i][w] = memo[i - 1][w]; //item not chosen
        }
    }
    return memo[n][L];
}

void print_dp() {
    int res = memo[n][L], w = L;
    vi ans;
    for (int i = n; i > 0 && res > 0; i--) {
        if (res != memo[i - 1][w]) {
            ans.push_back(i - 1);
            res -= V[i - 1];
            w -= W[i - 1];
        }
    }
    printf("%d %d\n",ans.size(),memo[n][L]);
    if (!ans.empty()) {
        for (int i = 0; i < ans.size(); i++) {
            printf("%d", ans[i]);
            if (i < ans.size() - 1) printf(" ");
        }
        printf("\n");
    }
}

// runs in O(nL) time
int main() {
    scanf("%d %d",&n,&L);
    //reset to -1
    for (int i = 0; i < n + 1; i++) {
        for (int j = 0; j < L; j++) memo[i][j] = -1;
    }
    for (int i = 0; i < n; i++) scanf("%d %d",&W[i],&V[i]);
    dp(0,L);
    print_dp();
    return 0;
}