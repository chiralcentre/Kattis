#include <bits/stdc++.h>

using namespace std;

typedef vector<char> vc;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string S; getline(cin,S);
    vc m;
    m.push_back(S[0]);
    char p = S[0];
    for (int i = 1; i < S.length(); i++) {
        if (S[i] != p) {
            m.push_back(S[i]);
            p = S[i];
        }
    }
    for (int i = 0; i < m.size(); i++) cout << m[i];
    return 0;
}