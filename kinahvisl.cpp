#include <bits/stdc++.h>

using namespace std;

string original, final;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> original >> final;
    int changes = 1;
    for (int i = 0; i < original.length(); i++) {
        if (original[i] != final[i]) changes++;
    }
    cout << changes << "\n";
    return 0;
}