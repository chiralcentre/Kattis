#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int N,M,L,R,best = 0,time_window = 0;

// code runs in O(N * 86400)
int main() {
    scanf("%d",&N);
    vi time_interval(86400, 0);
    for (int i = 0; i < N; i++) {
        scanf("%d",&M);
        for (int j = 0; j < M; j++) {
            scanf("%d %d",&L,&R);
            for (int k = L; k <= R; k++) { 
                time_interval[k]++;
                best = max(best, time_interval[k]);
            }
        }
    }
    printf("%d\n",best);
    for (int i = 0; i < 86400; i++) {
        if (time_interval[i] == best) time_window++;
    }
    printf("%d\n",time_window);
    return 0;
}