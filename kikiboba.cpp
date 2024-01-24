#include <bits/stdc++.h>

using namespace std;

unordered_map<char,int> counter = {{'b', 0}, {'k', 0}};
string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> s;
    for (char c: s) {
        if (counter.find(c) != counter.end()) counter[c]++;
    }
    if (counter['b'] == 0 && counter['k'] == 0) {
        cout << "none\n";
    } else if (counter['b'] < counter['k']) {
        cout << "kiki\n";
    } else if (counter['b'] > counter['k']) {
        cout << "boba\n";
    } else {
        cout << "boki\n";
    }
    return 0;
}