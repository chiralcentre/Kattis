#include <bits/stdc++.h>
#include <queue>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int n,m,pa,pb,u,v;
const int INF = 1e9;

int BFS(vvi &adjList) {
    vi D(n, INF); D[pa] = 0;
    queue<int> frontier; frontier.push(pa);
    while (!frontier.empty()) {
        int a = frontier.front();
        frontier.pop();
        for (int b: adjList[a]) {
            if (D[a] + 1 < D[b]) {
                frontier.push(b);
                D[b] = D[a] + 1;
                if (b == pb) return D[b];
            }
        }
    }
    return -1;
}

// perform BFS to find shortest path from Alice to Bob, divide by 2 and round up if necessary
// O(n + m) time
int main() {
    scanf("%d %d\n %d %d",&n,&m,&pa,&pb);
    vvi adjList(n, vi {});
    for (int i = 0; i < m; i++) {
        scanf("%d %d",&u,&v);
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }
    int res = BFS(adjList);
    printf("%d\n", res % 2 + res / 2);
    return 0;
}