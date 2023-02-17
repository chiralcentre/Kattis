#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

typedef vector<int> vi;
typedef unordered_set<int> usi;

int main() {
    int n,m; scanf("%d %d",&n,&m);
    vi pages(n,0), pred(n,-1), outdeg(n,0), CC;
    for (int i = 0; i < n; i++) scanf("%d",&pages[i]);
    for (int i = 0; i < m; i++) {
        int a,b; scanf("%d %d",&a,&b);
        a--; b--;
        pred[b] = a; outdeg[a]++;
    }
    for (int i = 0; i < n; i++) {
        if (outdeg[i] == 0) CC.push_back(i);
    }
    int lowest = 1000000000;
    for (int i = 0; i < CC.size(); i++) {
        int t = 0; usi read;
        int u = CC[i];
        while (u != -1) {
            t += pages[u];
            read.insert(u);
            u = pred[u];
        }
        for (int j = i + 1; j < CC.size(); j++) {
            int v = CC[j], temp = t;
            while (v != -1 && read.find(v) == read.end()) {
                temp += pages[v];
                v = pred[v];
            }
            lowest = min(lowest,temp);
        }
    }
    printf("%d\n",lowest);
    return 0;
}