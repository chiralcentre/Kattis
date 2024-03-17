#include <bits/stdc++.h>

using namespace std;

int n;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    vector<string> names(n, "");
    for (int i = 0; i < n; i++) cin >> names[i];
    int outputIndex = (12 % n);
    if (outputIndex != 0) swap(names[outputIndex], names[0]);
    for (int i = 0; i < n; i++) cout << names[i] << "\n";
    return 0;
}