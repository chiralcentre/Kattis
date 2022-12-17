#include <bits/stdc++.h>

using namespace std;

int main() {
    int N; scanf("%d",&N);
    vector<int> tea_prices(N);
    for (int i = 0; i < N; i++) scanf("%d", &tea_prices[i]);
    int M; scanf("%d",&M);
    vector<int> top_prices(M);
    for (int i = 0; i < M; i++) scanf("%d", &top_prices[i]);
    int lowest = 1000000000;
    for (int i = 0; i < N; i++) {
        int K; scanf("%d",&K);
        for (int j = 0; j < K; j++) {
            int t; scanf("%d",&t);
            int curr = tea_prices[i] + top_prices[t-1];
            if (curr < lowest) lowest = curr;
        }
    }
    int X; scanf("%d",&X);
    printf("%d\n",max(X/lowest - 1,0));
    return 0;
}