#include <bits/stdc++.h>

using namespace std;

typedef unordered_map<string,int> umsi;

int main() {
    umsi mappings;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, q; cin >> n >> q;
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        mappings[s] = i;
    }
    for (int i = 0; i < q; i++) {
        string a,b; cin >> a >> b;
        int u = mappings[a], v = mappings[b];
        cout << abs(u - v) - 1 << "\n";
    }
    return 0;
}