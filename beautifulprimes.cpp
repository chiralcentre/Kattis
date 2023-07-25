#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int T,N;

int main() {
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&N);
        vi ans(N,0);
        // keep taking the prime 7 and alternate with 11
        double d = 0;
        for (int i = 0; i < N; i++) {
            d += log10(7);
            ans[i] = 7;
            if (floor(d) + 1 < i + 1) {
                d += log10(11) - log10(7);
                ans[i] = 11;
            }
        }
        for (int i = 0; i < N - 1; i++) printf("%d ", ans[i]);
        printf("%d\n", ans[N - 1]);
    }
    return 0;
}