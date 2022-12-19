#include <bits/stdc++.h>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n; cin >> n;
    string code; cin >> code;
    string guess; cin >> guess;
    unordered_map<char,int> code_freq, guess_freq;
    int r = 0, s = 0;
    for (int i = 0; i < n; i++) {
        if (code[i] == guess[i]) r++;
        else {
            if (code_freq.count(code[i]) == 1) code_freq[code[i]]++;
            else code_freq[code[i]] = 1;
            if (guess_freq.count(guess[i]) == 1) guess_freq[guess[i]]++;
            else guess_freq[guess[i]] = 1;
        }
    }
    for (pair<char,int> p: code_freq) s += min(p.second,guess_freq[p.first]);
    cout << r << " " << s << "\n";
    return 0;
}