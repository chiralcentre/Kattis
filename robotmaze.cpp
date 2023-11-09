#include <bits/stdc++.h>
#include <deque>

using namespace std;

typedef pair<int,int> pii;
typedef tuple<int,int,int> iii;
typedef tuple<int,int,int,int> iiii;
typedef vector<string> vs;
typedef vector<iii> viii;

// note that directions 0 and 2 are opposite, directions 1 and 3 are opposite
int k,a,b,t,x[4] = {-1,0,1,0},y[4] = {0,1,0,-1}, opposite[4] = {2, 3, 0, 1}, visited[1000][1000][4][4];

bool inRange(int a, int b, int c) {return a >= b && a <= c;}

vector<iii> possiblepositions(int i, int j, int r, int c, vs &grid) {
    viii lst;
    for (int k = 0; k < 4; k++) {
        if (inRange(i + x[k], 0, r - 1) && inRange(j + y[k], 0, c - 1) && grid[i + x[k]][j + y[k]] != 'B') {
            lst.push_back(make_tuple(i + x[k], j + y[k], k));
        }
    }
    return lst;
}

pii findStart(vs &grid) {
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) 
        if (grid[i][j] == 'R') return make_pair(i,j);
    }
    return make_pair(-1,-1);
}

int solve(vs &grid, int r, int c) {
    // there are four directions to move from
    auto [i,j] = findStart(grid);
    deque<iiii> frontier;
    frontier.push_back(make_tuple(i,j,0,0));
    frontier.push_back(make_tuple(i,j,1,0));
    frontier.push_back(make_tuple(i,j,2,0));
    frontier.push_back(make_tuple(i,j,3,0));
    while (frontier.size() > 0) {
        auto [x,y,p,consec] = frontier.front();
        frontier.pop_front();
        // checking opposite is to check if robot is going back to cell where it came from
        for (auto &[a,b,np] : possiblepositions(x,y,r,c,grid)) {
            if ((p >= 0 && opposite[p] == np) || (np == p && consec == 2)) continue;
            t = consec;
            if (np != p) t = 0;
            if (visited[a][b][np][t + 1] == 0) {
                if (grid[a][b] == 'D') return visited[x][y][p][consec] + 1;
                visited[a][b][np][t + 1] = visited[x][y][p][consec] + 1;
                frontier.push_back(make_tuple(a,b,np,t+ 1));
            }
        }
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> k;
    while (k--) {
        cin >> a >> b;
        vs grid(a,"");
        for (int i = 0; i < a; i++) cin >> grid[i];
        memset(visited, 0, sizeof(visited));
        cout << solve(grid,a,b) << "\n";
    }
    return 0;
}