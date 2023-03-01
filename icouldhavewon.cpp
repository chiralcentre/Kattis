#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

//O(N^2) approach, where N is length of string
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s; cin >> s;
    vi verified;
    //check if each candidate for k can make Alice win more games
    for (int k = 1; k <= s.length(); k++) {
        int a = 0, b = 0, wA = 0, wB = 0;
        for (int i = 0; i < s.length(); i++) {
            (s[i] == 'A') ? a++ : b++;
            if (a == k || b == k) {
                (a == k) ? wA++ : wB++;
                a = 0, b = 0;
            }
        }
        if (wA > wB) verified.push_back(k);
    }
    cout << verified.size() << "\n";
    for (int i = 0; i < verified.size(); i++) {
        cout << verified[i];
        if (i < verified.size() - 1) cout << " ";
    }
}