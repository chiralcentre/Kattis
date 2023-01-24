#include <bits/stdc++.h>
#include <string>

using namespace std;

int main() {
    string s; cin >> s;
    int W = 0, B = 0;
    for (char c: s) {
        (c == 'W') ? W++ : B++;
    }
    cout << (B == W ? "1" : "0") << "\n";
    return 0;
}