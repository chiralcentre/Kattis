#include <bits/stdc++.h>

using namespace std;

int n,k;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> k;
    vector<string> names(n, "");
    for (int i = 0; i < n; i++) {
        cin >> names[i];
    }
    vector<int> toys(k, 0);
    for (int i = 0; i < k; i++) cin >> toys[i];
    // f(m) = (f(m-1) + L + 1) mod m,  L = toys[(n - m) % k]
    // f(1) = 0
    // modified Josephus recurrence for different elimination steps each round
    int pos = 0;
    int t = (n - 2) % k;                 // toy index for the m=2 round
    for (int m = 2; m <= n; m++) {
        pos += toys[t] + 1;
        if (pos >= m) pos %= m;          // pos < m-1 and L < m, so one subtract-free mod suffices
        if (--t < 0) t = k - 1;
    }
    cout << names[pos];
    return 0;
}