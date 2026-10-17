#include <bits/stdc++.h>
using namespace std;

int V;                      // number of distinct people appearing in conflict pairs
vector<vector<int>> adj;    // adj[v] = list of v's enemies
vector<int> color;          // color[v] = committee of v, or -1 if unassigned

bool ok(int v, int c) {
    for (int u : adj[v])
        if (color[u] == c) return false;
    return true;
}

// Try to colour vertices v..V-1 using at most k colours.
//
//   ncolors = how many DISTINCT colours vertices 0..v-1 are using.
//             Because of the rule below, those colours are always exactly
//             0, 1, ..., ncolors-1 with no gaps, so the lowest colour not
//             yet used is simply index `ncolors`.
//             It is path-dependent: each branch passes its own value down,
//             so two different partial colourings reach this line with
//             different budgets.
//
//   limit   = one past the highest colour v is allowed to try, i.e. v may
//             take any colour in {0, ..., ncolors} — every colour already
//             in use, plus ONE fresh one.
//             Capped at k because colour index k does not exist when we are
//             testing whether k colours suffice.
//
// Why only one fresh colour: an unused colour has no contents, so all unused
// colours are interchangeable. Trying ncolors+1 would re-run the search we
// already ran for ncolors, with the two labels swapped.
bool dfs(int v, int k, int ncolors) {
    if (v == V) return true;        // every vertex placed — success

    int limit = min(ncolors + 1, k);

    for (int c = 0; c < limit; c++) {
        if (!ok(v, c)) continue;    // an enemy of v already sits in committee c

        color[v] = c;

        // New distinct-colour count for the subtree below:
        //   reused an old colour (c < ncolors)   -> c+1 <= ncolors, stays ncolors
        //   took the fresh colour (c == ncolors) -> becomes ncolors+1
        if (dfs(v + 1, k, max(ncolors, c + 1))) return true;

        color[v] = -1;              // undo, restoring the sentinel
    }
    return false;                   // no colour worked for v under this prefix
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    while (cin >> n >> m && (n || m)) {
        unordered_map<string, int> id;
        adj.assign(n + 1, {}); 
        V = 0;

        for (int i = 0; i < m; i++) {
            string a, b;
            cin >> a >> b;
            if (!id.count(a)) id[a] = V++;
            if (!id.count(b)) id[b] = V++;
            int u = id[a], w = id[b];
            adj[u].push_back(w);
            adj[w].push_back(u);
        }

        color.assign(V, -1);

        // Iterative deepening: smallest k that admits a valid colouring.
        int k = 1;
        while (!dfs(0, k, 0)) k++;

        cout << k << "\n";
    }
    return 0;
}