#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string ciphertext, secret; cin >> ciphertext >> secret;
    vector<char> ans;
    for (int i = 0; i < min(secret.length(),ciphertext.length()); i++) {
        ans.push_back((ciphertext[i] - secret[i] + 26) % 26 + 'A');
    }
    for (int i = secret.length(); i < ciphertext.length(); i++) {
        ans.push_back((ciphertext[i] - ans[i - secret.length()] + 26) % 26 + 'A');
    }
    for (char c: ans) cout << c;
    return 0;
}