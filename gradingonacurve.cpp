#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
int N,T,M; vi scores(100000,0);


bool satisfy_conds(int K) {
    int first = 0, second = 0, third = 0;
    for (int i = 0; i < N; i++) {
        if (scores[i] * 10 >= 7 * K) third ++;
        if (scores[i] * 10 >= 8 * K) second ++;
        if (scores[i] * 10 >= 9 * K) first ++;
    }
    return first * 4 >= N && second * 2 >= N && third * 4 >= 3 * N;
}

int main() {
    scanf("%d %d",&N,&T);
    for (int i = 0; i < N; i++) scanf("%d",&scores[i]);
    int L = 1, H = T << 1, ans = -1;
    while (L <= H) {
        M = L + ((H - L) >> 1);
        if (satisfy_conds(M)) ans = M, L = M + 1;
        else H = M - 1;
    }
    printf("%d\n",ans);
    return 0;
}