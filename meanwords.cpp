#include <bits/stdc++.h>

using namespace std;

typedef vector<string> vs;
typedef vector<char> vc;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N; cin >> N;
    vs words; int h = -1;
    for (int i = 0; i < N; i++) {
        string s; cin >> s;
        words.push_back(s);
        h = max(h, (int) s.length());
    }
    vc ans;
    for (int i = 0; i < h; i++) {
        int total = 0, count = 0;
        for (int j = 0; j < N; j++) {
            if (words[j].length() > i) {
                total += words[j][i];
                count++;
            }
        }
        ans.push_back(char(total / count));
    }
    for (char c: ans) cout << c;
    return 0;
}