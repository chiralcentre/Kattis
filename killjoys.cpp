#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

vector<vector<int>> adjList;
vector<int> colour;
vector<int> components;
bool isBipartite = true;

void DFS(int u, int c, int L) {
    components[u] = L;

    if (colour[u] != 2) {
        if (colour[u] != c) {
            isBipartite = false;
        }
        return;
    }

    colour[u] = c;

    for (int v : adjList[u]) {
        if (c == 1)
            DFS(v, 0, L);
        else
            DFS(v, 1, L);
    }
}

ll modPow(ll base, ll exp, ll mod) {
    ll result = 1;

    while (exp > 0) {
        if (exp & 1)
            result = result * base % mod;

        base = base * base % mod;
        exp >>= 1;
    }

    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N, M, p;
    cin >> N >> M >> p;

    adjList.assign(N, {});
    colour.assign(N, 2);
    components.assign(N, -1);

    for (ll i = 0; i < M; i++) {
        ll u, v;
        cin >> u >> v;
        u--; v--;
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }

    ll CC = 0;

    for (ll u = 0; u < N; u++) {
        if (isBipartite && colour[u] == 2) {
            DFS(u, 0, CC);
            CC++;
        }
    }

    if (!isBipartite) {
        cout << "impossible\n";
    } else {
        cout << (modPow(2, CC - 1, p) + 1) % p << '\n';
    }

    return 0;
}