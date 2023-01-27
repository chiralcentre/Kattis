#include <bits/stdc++.h>

using namespace std;

typedef unordered_map<int,char> mic;
typedef unordered_map<char,int> mci;

mic alphabet; mci reverseAlphabet;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    for (int i = 0; i < 26; i++) {
        alphabet[i] = i + 'A';
        reverseAlphabet[i + 'A'] = i;
    }
    alphabet[26] = '_', alphabet[27] = '.';
    reverseAlphabet['_'] = 26, reverseAlphabet['.'] = 27;
    while (true) {
        int N; cin >> N;
        if (N == 0) break;
        string t; cin >> t;
        vector<char> ans; int L = t.length();
        for (int i = 0; i < L; i++) {
            ans.push_back(alphabet[(reverseAlphabet[t[L - i - 1]]  + N) % 28]);
        }
        for (char c: ans) cout << c;
        cout << "\n";
    }
    return 0;
}