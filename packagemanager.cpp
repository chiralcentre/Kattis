#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef unordered_map<string,int> umsi;

int b,t,v; string p;
vi stores(1001,0);
umsi packageVersions;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> t >> b;
    for (int i = 0; i < b; i++) cin >> stores[i];
    for (int i = 0; i < t; i++) {
        cin >> p >> v;
        packageVersions[p] = v;
    }
    for (int i = 0; i < b; i++) {
        int ans = 0;
        for (int j = 0; j < stores[i]; j++) {
            cin >> p >> v;
            ans += packageVersions[p] - v;
        }
        cout << ans << "\n";
    }
    return 0;
}