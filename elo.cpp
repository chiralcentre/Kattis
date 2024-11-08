#include <bits/stdc++.h>
using namespace std;

int n,x;
int L[1050];
int R[1050];
int A[1050];
int visited[6000];

void solve(int elo) {
    if (visited[elo]) return;
    visited[elo] = 1;
    for (int i = 0; i < n; i++) {
        if (L[i] <= elo && elo <= R[i]) solve(elo + A[i]);
    }
}

int main() {
    memset(visited,0,sizeof(visited));
    scanf("%d %d",&n, &x);
    for (int i = 0; i < n; i++) scanf("%d %d %d",&L[i],&R[i],&A[i]);
    solve(x);
    int best = 0;
    for (int i = 0; i < 6000; i++) if(visited[i]) best = i;
    printf("%d\n",best);
    return 0;
}