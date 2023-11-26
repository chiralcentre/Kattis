#include <bits/stdc++.h>

using namespace std;

string s,d = "|";

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector<string> words;
    while (getline(cin, s)) {
        int p = s.find(d);
        words.push_back(s.substr(0,p));
        words.push_back(s.substr(p + 1));
    }
    cout << words[0] + words[2] << " " << words[1] + words[3] << "\n";
    return 0;
}