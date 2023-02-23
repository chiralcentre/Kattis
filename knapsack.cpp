#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int memo[2001][2001], V[2001], W[2001];
int C,n;

//bottom up DP
int dp(int id, int remW) {
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= C; w++) {
            if (i == 0 || w == 0) memo[i][w] = 0;
            else if (W[i - 1] <= w) memo[i][w] = max(V[i - 1] + memo[i - 1][w - W[i - 1]], memo[i - 1][w]); //choose one item
            else memo[i][w] = memo[i - 1][w]; //item not chosen
        }
    }
    return memo[n][C];
}

void print_dp() {
    int res = memo[n][C], w = C;
    vi ans;
    for (int i = n; i > 0 && res > 0; i--) {
        if (res != memo[i - 1][w]) {
            ans.push_back(i - 1);
            res -= V[i - 1];
            w -= W[i - 1];
        }
    }
    printf("%d\n",ans.size());
    if (!ans.empty()) {
        for (int i = 0; i < ans.size(); i++) {
            printf("%d", ans[i]);
            if (i < ans.size() - 1) printf(" ");
        }
        printf("\n");
    }
}

int main() {
    while (scanf("%d %d",&C,&n) == 2) {
        //reset to -1
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < 2001; j++) memo[i][j] = -1;
        }
        for (int i = 0; i < n; i++) scanf("%d %d",&V[i],&W[i]);
        dp(0,C);
        print_dp();
    } 
    return 0;
}