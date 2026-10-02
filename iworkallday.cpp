#include <bits/stdc++.h>

using namespace std;

int N,T;

int main() {
    scanf("%d",&N);
    vector<int> settings(N,0);
    for (int i = 0; i < N; i++) scanf("%d",&settings[i]);
    scanf("%d",&T);
    int best = 1e9, ans = -1;
    for (int s: settings) {
        int r = T % s;
        if (r < best) {
            best = r;
            ans = s;
        }
    }
    printf("%d\n",ans);
    return 0;
}