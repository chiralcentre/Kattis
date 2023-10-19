#include <bits/stdc++.h>

using namespace std;

const int MAXR = 501, MAXS = 501, INF = 1000000000;

// above[a][b] stores the row of the closest tree above (a,b) in column b
// below[a][b] stores the row of the closest tree below (a,b) in column b
int R, S, G;
char grid[MAXR][MAXS];
int above[MAXR][MAXS], below[MAXR][MAXS];

int dist(int x1, int y1, int x2, int y2) {return (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2);}

// update above and below arrays for particular column
void update(int col) {
    int a = -1, b = -1;
    for(int i = 0; i < R; i++) {
        if (grid[i][col] == 'x') a = i;
        above[i][col] = a;
    }
    for(int i = R - 1; i >= 0; i--) {
        if(grid[i][col] == 'x') b = i;
        below[i][col] = b;
    }
}

int solve(int r, int c) {
    int ans = INF;
    for (int i = 0; i < S; i++) {
        if (above[r][i] != -1) ans = min(ans, dist(r, c, above[r][i], i));
        if (below[r][i] != -1) ans = min(ans, dist(r, c, below[r][i], i));
    }
    return ans;
}

int main() {
    scanf("%d %d", &R, &S);
    for (int i = 0; i < R; i++) scanf("%s", grid[i]);
    for (int i = 0; i < S; i++) update(i);
    scanf("%d", &G);
    for(int i = 0; i < G; ++i) {
        int r, c; scanf("%d %d", &r, &c);
        r--; c--;
        printf("%d\n", solve(r, c));
        grid[r][c] = 'x';
        update(c);
    }
    return 0;
}
