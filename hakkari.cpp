#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;
typedef vector<pii> vpii;

int n,m;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    vector<string> grid(n, "");
    for (int i = 0; i < n; i++) cin >> grid[i];
    vpii mines;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '*') mines.push_back({i + 1,j + 1});
        }
    }
    cout << mines.size() << "\n";
    for (auto &[x,y]: mines) cout << x << " " << y << "\n";
    return 0;
}