#include <bits/stdc++.h>

using namespace std;

typedef vector<vector<int>> VVI;
typedef vector<int> VI;

int MinCostMatching(const VVI &cost, VI &Lmate, VI &Rmate) {
  int n = int(cost.size());

  // construct dual feasible solution
  VI u(n);
  VI v(n);
  for (int i = 0; i < n; i++) {
    u[i] = cost[i][0];
    for (int j = 1; j < n; j++) u[i] = min(u[i], cost[i][j]);
  }
  for (int j = 0; j < n; j++) {
    v[j] = cost[0][j] - u[0];
    for (int i = 1; i < n; i++) v[j] = min(v[j], cost[i][j] - u[i]);
  }
  
  // construct primal solution satisfying complementary slackness
  Lmate = VI(n, -1);
  Rmate = VI(n, -1);
  int mated = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (Rmate[j] != -1) continue;
      if (cost[i][j] == u[i] + v[j]) {
        Lmate[i] = j;
        Rmate[j] = i;
        mated++;
        break;
      }
    }
  }
  
  VI dist(n);
  VI dad(n);
  VI seen(n);
  
  // repeat until primal solution is feasible
  while (mated < n) {
    
    // find an unmatched left node
    int s = 0;
    while (Lmate[s] != -1) s++;
    
    // initialize Dijkstra
    fill(dad.begin(), dad.end(), -1);
    fill(seen.begin(), seen.end(), 0);
    for (int k = 0; k < n; k++) dist[k] = cost[s][k] - u[s] - v[k];
    
    int j = 0;
    while (true) {
      
      // find closest
      j = -1;
      for (int k = 0; k < n; k++) {
        if (seen[k]) continue;
        if (j == -1 || dist[k] < dist[j]) j = k;
      }
      seen[j] = 1;
      
      // termination condition
      if (Rmate[j] == -1) break;
      
      // relax neighbors
      const int i = Rmate[j];
      for (int k = 0; k < n; k++) {
        if (seen[k]) continue;
        const int new_dist = dist[j] + cost[i][k] - u[i] - v[k];
        if (dist[k] > new_dist) {
            dist[k] = new_dist;
            dad[k] = j;
        }
      }
    }
    
    // update dual variables
    for (int k = 0; k < n; k++) {
      if (k == j || !seen[k]) continue;
      const int i = Rmate[k];
      v[k] += dist[k] - dist[j];
      u[i] -= dist[k] - dist[j];
    }
    u[s] += dist[j];
    
    // augment along path
    while (dad[j] >= 0) {
      const int d = dad[j];
      Rmate[j] = Rmate[d];
      Lmate[Rmate[j]] = j;
      j = d;
    }
    Rmate[j] = s;
    Lmate[s] = j;
    
    mated++;
  }
  
  int value = 0;
  for (int i = 0; i < n; i++) {
    value += cost[i][Lmate[i]];
    if (cost[i][Lmate[i]] == 11) { // edge does not exist
      int j = Lmate[i];
      Lmate[i] = Rmate[j] = -1; // set to unmatched
      value -= 11;
    }
  }
  return value;
}


int main() {
    int n,m,r,a,b,c,unmatched = 0;
    scanf("%d %d %d",&n,&m,&r);
    VI lmate, rmate;
    // default value of 11 means edge does not exist
    VVI cost(n + m, VI(n + m, 11));
    // problem topics have indices 0 to n - 1, problem proposals have indices n to n + m - 1
    for (int i = 0; i < r; i++) {
        scanf("%d %d %d",&a,&b,&c);
        a--; b--;
        cost[a][b + n] = -c;
    }
    int res = -MinCostMatching(cost,lmate,rmate);
    for (int i = 0; i < n; i++) unmatched += (lmate[i] == -1);
    printf("%d %d\n", unmatched, res);
    return 0;
}