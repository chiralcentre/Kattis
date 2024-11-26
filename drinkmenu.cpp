#include <bits/stdc++.h>

using namespace std;

int n,m; string c;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    cin.ignore();
    vector<string> drinks(n, "");
    unordered_map<string,int> customers;
    for (int i = 0; i < n; i++) getline(cin, drinks[i]);
    for (int i = 0; i < m; i++) {
        getline(cin, c);
        if (customers.find(c) == customers.end()) {
            cout << drinks[0] << "\n";
            customers[c] = 1;
        } else {
            cout << drinks[customers[c]] << "\n";
            customers[c]++;
        }
    }
    return 0;
}