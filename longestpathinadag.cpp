#include <bits/stdc++.h>
#include <queue>

using namespace std;

const int INF = 1000000000;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef queue<int> qi;

/* preconditions:
1) graph must be directed acyclic
2) adjList is a list of lists representing the graph in adjaceny list form
3) indeg is a list of length V where indeg[v] represents the indegree of vertex v
postconditions:
1) indeg array is modified such that every entry is now 0
2) returns an list of vertices in topological order 
*/
vi kahnsAlgorithm(vvi adjList, vi indeg) {
    qi frontier;
    for (int i = 0; i < indeg.size(); i++) {
        if (indeg[i] == 0) frontier.push(i);
    }
    vi toposort;
    while (!frontier.empty()) {
        int u = frontier.front(); frontier.pop();
        toposort.push_back(u);
        for (int v: adjList[u]) {
            if (--indeg[v] == 0) frontier.push(v);
        }
    }
    return toposort;
}

int main() {
    int V,E; scanf("%d %d",&V,&E);
    vvi adjList(V, vi {}); vi indeg(V,0);
    for (int i = 0; i < E; i++) {
        int u,v; scanf("%d %d",&u,&v);
        u--;v--;
        adjList[u].push_back(v);
        indeg[v]++;
    }
    //longest path must start from vertices with 0 indeg
    vi d(V,INF), p(V,-1);
    for (int i = 0; i < V; i++) { 
        if(indeg[i] == 0) d[i] = 0;
    }
    //carry out toposort with Kahn's algorithm in O(V + E) time
    vi toposort = kahnsAlgorithm(adjList,indeg);
    //relax edges in topological order
    for (int u: toposort) {
        if (d[u] != INF) {
            for (int v: adjList[u]) {
                if (d[v] > d[u] - 1) { // negate edges, edge weight = -1
                    d[v] = d[u] - 1;
                    p[v] = u;
                }
            }
        }
    }
    //find ending vertex on longest path
    int lowest = 1, index = -1;
    for (int i = 0; i < V; i++) {
        if (d[i] < lowest) {
            index = i;
            lowest = d[i];
        }
    }
    //reconstruct path
    vi path;
    while (p[index] != -1) {
        path.push_back(index);
        index = p[index];
    }
    path.push_back(index);
    printf("%d\n",path.size());
    for (int i = path.size() - 1; i >= 0; i--) {
        printf("%d",path[i] + 1);
        if (i > 0) printf(" ");
    }
    printf("\n");
    return 0;
}