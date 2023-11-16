#include <bits/stdc++.h>
#include <queue>

using namespace std;

typedef long long ll;
typedef vector<bool> vb;
typedef pair<int,int> ii;

int m,n,s,t,a[10],b[10];

int solve() {
    queue<ii> frontier;
    frontier.push({s,0});
    vb visited(m,false);
    visited[s] = true;
    while (!frontier.empty()) {
        auto [u,c] = frontier.front();
        frontier.pop();
        for (int i = 0; i < n; i++) {
            t = int((ll(u) * ll(a[i]) + ll(b[i])) % m);
            if (!visited[t]) {
                if (t == 0) return c + 1;
                visited[t] = true;
                frontier.push({t,c + 1});
            }
        }
    }
    return -1;
}

int main() {
    scanf("%d %d %d",&m,&n,&s);
    for (int i = 0; i < n; i++) scanf("%d %d",&a[i],&b[i]);
    printf("%d\n",solve());
    return 0;
}