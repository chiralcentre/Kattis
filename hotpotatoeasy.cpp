#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp> // Common file 
#include <ext/pb_ds/tree_policy.hpp> 
#include <functional> // for less 

using namespace __gnu_pbds;
using namespace std;

// only compare first integer key, which is guaranteed to be unique
struct cmp {
    bool operator()(const pair<int, string>& a,
                    const pair<int, string>& b) const {
        return a.first < b.first;
    }
};

typedef tree<pair<int, string>, null_type, cmp, rb_tree_tag,
             tree_order_statistics_node_update> ordered_set;

int n,k;
string name;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> k;
    ordered_set S;
    for (int i = 0; i < n; i++) {
        cin >> name;
        S.insert({i, name});
    }
    vector<int> toys(k, 0);
    for (int i = 0; i < k; i++) cin >> toys[i];
    int player_idx = 0, toy_idx = 0;
    while (S.size() > 1) {
        int L = toys[toy_idx];
        player_idx = (player_idx + L) % S.size();
        S.erase(S.find_by_order(player_idx));
        if (player_idx == S.size()) player_idx = 0; // wrap around
        toy_idx = (toy_idx + 1) % k;
    }
    cout << S.begin()->second;
    return 0;
}