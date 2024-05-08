#include <bits/stdc++.h>

using namespace std;

typedef vector<string> vs;

int n;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    vs parts(n, "");
    for (int i = 0; i < n; i++) cin >> parts[i];
    for (int i = n - 1; i >= 0; i--) {
        for (int j = parts[i].length() - 1; j >= 0; j--) cout << parts[i][j];
    }
    cout << "\n";
    return 0;
}