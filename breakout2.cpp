#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;;

int n,x,m,s;

// only two ways; either clockwise or anticlockwise
int main() {
    scanf("%d %d %d",&n,&x,&m);
    x--;
    vi costs(n, 0);
    for (int i = 0; i < m; i++) {
        scanf("%d",&s);
        costs[s - 1]++;
    }
    int cw = 0, rcw = costs[n - 1];
    for (int i = 0; i < x; i++) cw += costs[i];
    for (int i = n - 1; i > x; i--) rcw += costs[i - 1];
    printf("%d\n", min(cw, rcw));
    return 0;
}