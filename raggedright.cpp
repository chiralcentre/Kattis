#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

string s; int m = -1;
vi lengths;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    while (getline(cin, s)) {
        m = max(m, int(s.length()));
        lengths.push_back(int(s.length()));
    }
    int ans = 0;
    for (int i = 0; i < lengths.size() - 1; i++) ans += (m - lengths[i]) * (m - lengths[i]);
    cout << ans << "\n";
    return 0;
}