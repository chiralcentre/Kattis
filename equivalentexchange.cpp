#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int d; cin >> d;

    unordered_map<int, vector<int>> mp;
    // reserve capacity to avoid unnecessary rehashes
    mp.reserve(d * 2);

    int i = 0;
    for (int day = 0; day < d; ++day) {
        int q; cin >> q;
        if (q == 1) {
            int f; cin >> f;
            mp[f].push_back(i);
            ++i;
        } else {
            int s, e; cin >> s >> e;
            auto it = mp.find(s);
            if (it == mp.end()) continue;
            vector<int> a = move(it->second);
            mp.erase(it);
            vector<int> &b = mp[e];
            if (b.size() < a.size()) b.swap(a);
            b.insert(b.end(), a.begin(), a.end());
        }
    }

    vector<int> results(i);
    for (auto &kv : mp)
        for (int v : kv.second)
            results[v] = kv.first;

    for (int v : results)
        cout << v << '\n';
}