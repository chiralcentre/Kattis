#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef unordered_map<int,int> mii;
typedef unordered_map<ll,int> mli;
typedef unordered_map<int,vi> mvi;

int A[100000], B[100000],N,M,D;
ll u,v,r;
vvi adjList(100000, vi {}); vi ts, C;
bool visited[100000];
const int INF = 1e9;

void toposort(int u) {
    visited[u] = true;
    for (int v: adjList[u]) {
        if (!visited[v]) toposort(v);
    }
    ts.push_back(u);
}

int LIS(int N) {
    if (N == 0) return 0;
    vi L; L.push_back(C[0]);
    for (int i = 1; i < N; i++) {
        //add to LIS
        if (C[i] > L.back()) L.push_back(C[i]);
        //replace with better candidate
        else {
            int pos = lower_bound(L.begin(), L.end(), C[i]) - L.begin();
            L[pos] = C[i];
        }
    }
    return L.size();
}

// perform topological sort to produce the rankings, R
// find LCS of R and the rankings provided, denoted as L
// ans = (N - L) * 2
int main() {
    scanf("%d %d %d", &N, &M, &D);
    // construct graph
    // take in edge points as long longs since they can exceed integer limit
    mli pandaMappings;
    int counter = 0;
    for (int i = 0; i < M; i++) {
        scanf("%lld %lld", &u, &v);
        if (pandaMappings.find(u) == pandaMappings.end()) pandaMappings[u] = counter++;
        if (pandaMappings.find(v) == pandaMappings.end()) pandaMappings[v] = counter++;
        adjList[pandaMappings[u]].push_back(pandaMappings[v]);
    }
    // perform toposort using recursive DFS
    for (int i = 0; i < N; i++) {
        if (!visited[i]) toposort(i);
    }
    reverse(ts.begin(), ts.end());
    for (int i = 0; i < N; i++) A[i] = ts[i]; //transfer over to array A
    // take in provided rank list
    for (int i = 0; i < N; i++) {
        scanf("%lld",&r);
        B[i] = (pandaMappings.find(r) == pandaMappings.end()) ? -1 : pandaMappings[r];
    }
    // find LCS of the two sequences
    mii A_mappings;
    for (int i = 0; i < N; i++) A_mappings[A[i]] = i;
    //time complexity = O(N log N)
    //record position of each element in A in B into C in descending order
    //LCS of A and B is the longest increasing subsequence of C
    mvi B_mappings;
    for (int j = 0; j < N; j++) {
        if (B_mappings.find(B[j]) == B_mappings.end()) B_mappings[B[j]] = vi {j};
        else B_mappings[B[j]].push_back(j);
    }
    for (int i = 0; i < N; i++) {
        if (B_mappings.find(A[i]) != B_mappings.end()) {
            for (int j = B_mappings[A[i]].size() - 1; j >= 0; j--) C.push_back(B_mappings[A[i]][j]);
        }
    }
    printf("%d\n", (N - LIS(int(C.size()))) << 1);
    return 0;
}