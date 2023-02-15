#include <bits/stdc++.h>

using namespace std;

int set_bits(int n) {
    int count = 0;
    while (n != 0) {
        n &= n - 1;
        count++;
    }
    return count;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T; cin >> T;
    while (T--) {
        string X; cin >> X;
        int highest = -1;
        for (int i = 1; i <= X.length(); i++) highest = max(highest,set_bits(stoi(X.substr(0,i))));
        cout << highest << "\n";
    }
    return 0;
}