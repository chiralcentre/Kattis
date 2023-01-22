#include <bits/stdc++.h>

using namespace std;

typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vvi;

void DFS(int s, vvi &components, vb &visited, vvi &adjList) {
    visited[s] = true;
    vi lst,frontier;
    lst.push_back(s); frontier.push_back(s);
    while (!frontier.empty()) {
        int u = frontier.back(); frontier.pop_back();
        for (int v: adjList[u]) {
            if (!visited[v]) {
                visited[v] = true;
                lst.push_back(v);
                frontier.push_back(v);
            }
        }
    }
    components.push_back(lst);
}

int main() {
    int N; scanf("%d",&N);
    vi adjList(N,0), indeg(N,0); vvi UDadjList(N,vi{});
    for (int i = 0; i < N; i++) {
        int a; scanf("%d",&a);
        adjList[i] = --a; indeg[a]++;
        UDadjList[i].push_back(a); UDadjList[a].push_back(i);
    }
    vvi components; vb visited(N,false);
    for (int i = 0; i < N; i++) {
        if (!visited[i]) DFS(i,components,visited,UDadjList);
    }
    int assignments = 0;
    for (vi lst: components) {
        int counter = 0;
        for (int u: lst) {
            if (indeg[u] > 1) counter += indeg[u] - 1;
        }
        assignments += components.size() > 1 ? max(counter,1) : counter;
    }
    printf("%d\n",assignments);
    return 0;
}