#include <bits/stdc++.h>

using namespace std;

string s,w = "UAPC";

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> s;
    for (char c: w) if (s.find(c) == -1) cout << c;
    return 0;
}