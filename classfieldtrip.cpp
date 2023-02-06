#include <bits/stdc++.h>

using namespace std;

typedef vector<char> vc;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string a,b; cin >> a >> b;
    vc c(a.begin(), a.end());
    for (int i = 0; i < b.length(); i++) c.push_back(b[i]);
    sort(c.begin(),c.end());
    for (char ch: c) cout << ch;
    cout << "\n";
    return 0;
}