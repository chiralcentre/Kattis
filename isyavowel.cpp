#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

string s;
unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> s;
    int v = 0, y = 0;
    for (char c: s) {
        if (vowels.find(c) != vowels.end()) v++;
        else if (c == 'y') y++;
    }
    cout << v << " " << v + y << "\n";
    return 0;
}