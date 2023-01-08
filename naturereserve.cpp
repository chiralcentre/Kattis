#include <bits/stdc++.h>
#include <queue>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vii> AL;
typedef long long ll;

int main() {
    int D; scanf("%d",&D);
    while (D--) {
        ll N,M,L,S; scanf("%lld %lld %lld %lld",&N,&M,&L,&S);
        vi frontier; 
        for (int i = 0; i < S; i++) {
            int s; scanf("%d",&s);
            frontier.push_back(--s);
        }
        AL adjList(N, vii {}); vector<bool> taken(N, false);
        for (int i = 0; i < M; i++) {
            int u,v,w; scanf("%d %d %d",&u,&v,&w);
            u--; v--;
            adjList[u].push_back(make_pair(v,w));
            adjList[v].push_back(make_pair(u,w));
        }
        //run Prim's algorithm from the S stations and ensure n - S edges are chosen in O(M log N)
        //answer =  cost of N - S edges + (N - S) * L
        ll cost = 0; int E = 0;
        priority_queue<ii> PQ;
        //since C++ priority queue is max heap, negation is required to convert to min heap
        for (int u: frontier) {
            for (auto &[v,w]: adjList[u]) {
                PQ.emplace(-w,-v); // sort by increasing weight and increasing ID
                taken[u] = true;
            }
        }
        while (!PQ.empty() && E < N - S) {
            auto [w,u] = PQ.top(); PQ.pop();
            w = -w; u = -u;
            if (!taken[u]) {
                cost += w; E += 1;
                taken[u] = true;
                for (auto &[v,w2]: adjList[u]) {
                    if (!taken[v]) PQ.emplace(-w2,-v);
                }
            }
        }
        printf("%lld\n",cost + (N - S) * L);
    }
    return 0;
}