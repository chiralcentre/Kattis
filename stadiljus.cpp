#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int N,x,y;

int main() {
    scanf("%d\n%d\n%d",&N,&x,&y);
    vi strips(N,0);
    for (int i = 0; i < N; i++) scanf("%d",&strips[i]);
    sort(strips.begin(), strips.end());
    int curr = 0, best = 0;
    for (int i = 0; i < N; i++) {
        curr += strips[i] * x;
        if (curr > (i + 1) * y) break;
        best = i + 1;
    }
    printf("%d\n",best);
    return 0;
}