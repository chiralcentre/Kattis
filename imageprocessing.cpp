#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;

int H,W,N,M;

int main() {
    scanf("%d %d %d %d",&H,&W,&N,&M);
    vii image(H, vi(W, 0));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            scanf("%d",&image[i][j]);
        }
    }
    vii kernel(N, vi(M, 0));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%d",&kernel[i][j]);
        }
    }
    vii ans(H - N + 1, vi(W - M + 1));
    for (int i = 0; i < H - N + 1; i++) {
        for (int j = 0; j < W - M + 1; j++) {
            int res = 0;
            for (int k = 0; k < N; k++) {
                for (int m = 0; m < M; m++) {
                    res += image[i + k][j + m] * kernel[N - k - 1][M - m - 1];
                }
            }
            ans[i][j] = res;
        }
    }
    for (int i = 0; i < H - N + 1; i++) {
        for (int j = 0; j < W - M + 1; j++) {
            printf("%d",ans[i][j]);
            if  (j < W - M) printf(" ");
        }
        printf("\n");
    }
    return 0;
}