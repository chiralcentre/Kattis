#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int main() {
    int n,m; scanf("%d %d",&n,&m);
    vvi grid(n,vi(m,0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d",&grid[i][j]);
        }
    }
    int lowest = 1e9;
    // go through all possible points in grid in O(n^2*m^2) time
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int temp = 0;
            for (int k = 0; k < n; k++) {
                for (int p = 0; p < m; p++) {
                    temp += (abs(k - i) + abs(p - j)) * grid[k][p];
                }
            }
            lowest = min(temp,lowest);
        }
    }
    printf("%d\n",lowest);
    return 0;
}