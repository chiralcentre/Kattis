#include <bits/stdc++.h>
#include <string>

using namespace std;

int addToCounter(unordered_map<char,string> mappings, string S, string w) {
    for (int i = 0; i < S.length(); i++) {
        if (mappings[S[i]].find(w[i]) >= mappings[S[i]].length()) {
            return 0;
        }
    }
    return 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N; cin >> N;
    unordered_map<char,string> mappings;
    mappings['1'] = ""; mappings['2'] = "abc"; mappings['3'] = "def";
    mappings['4'] = "ghi"; mappings['5'] = "jkl"; mappings['6'] = "mno";
    mappings['7'] = "pqrs"; mappings['8'] = "tuv"; mappings['9'] = "wxyz";
    vector<string> words(N,"");
    for (int i = 0; i < N; i++) cin >> words[i];
    string S; cin >> S;
    int counter = 0;
    for (string w: words) {
        if (w.length() == S.length()) {
            counter += addToCounter(mappings,S,w);
        }
    }
    cout << counter << "\n";
    return 0;
}