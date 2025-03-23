#include <bits/stdc++.h>

using namespace std;

bool grid[501][501];

int n,xa,ya,xb,yb;

// code runs in O(t * n * 250000) time
int main() {
    while (true) {
        scanf("%d",&n);
        if (n == 0) break;
        memset(grid, 0, sizeof(grid));
        int total = 0; 
        for (int m = 0; m < n; m++) {
            scanf("%d %d %d %d",&xa,&ya,&xb,&yb);
            for (int i = xa; i < xb; i++) {
                for (int j = ya; j < yb; j++) {
                    if (!grid[i][j]) {
                        grid[i][j] = true;
                        total++;
                    }
                }
            }
        }
        printf("%d\n", total);
    }
    return 0;
}