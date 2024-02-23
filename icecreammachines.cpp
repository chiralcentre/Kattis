#include <bits/stdc++.h>
#include <queue>
#include <set>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef queue<int> qi;
typedef vector<qi> vqi;

int n,m,k;

int main() {
    scanf("%d %d %d",&n,&m,&k);
    // flavours[i] represents the indices of the customers that want the ith flavour
    // flavours[i] is naturally in sorted order
    vqi flavours(m, qi {}); vi orders(n, -1);
    for (int i = 0; i < n; i++) {
        scanf("%d",&orders[i]); orders[i]--;
        flavours[orders[i]].push(i);
    }
    // suppose we are processing customer i and have the choice between using two machines which have loaded the flavours a and b respectively.
    // consider the next time a and b appears in the input after index i
    // a greedy solution should replace the flavour which comes farthest in the future
    // O (n log k)
    int ans = 0; set<ii> iceCreamMachines;
    vi taken(m, -1);
    for (int i = 0; i < m; i++) {
        // remove first index from every queue, such that now the queue for ith flavour has the next index of the customer at the front
        if (flavours[i].size() > 0) flavours[i].pop(); 
    }
    for (int i = 0; i < n; i++) {
        int c = orders[i];
        // currently no ice cream machine is loaded with flavour c
        if (taken[c] == -1) {
            if (iceCreamMachines.size() == k) { // all ice cream machines are loaded 
                ii p = *iceCreamMachines.rbegin();
                iceCreamMachines.erase(p);
                taken[p.second] = -1;
            }
            ans++;
        } else iceCreamMachines.erase(make_pair(taken[c], c));
        if (flavours[c].size() > 0) {
            taken[c] = flavours[c].front();
            flavours[c].pop();
            iceCreamMachines.insert(make_pair(taken[c], c));
        }
    }
    printf("%d\n",ans);
    return 0;
}