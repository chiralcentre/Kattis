#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <cmath>
#include <iomanip>

using namespace std;

int N; string a, s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '";;
unordered_map<char,int> alphabet;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    getline(cin, a);
    N = stoi(a);
    for (int i = 0; i < 28; i++) alphabet[s[i]] = i;
    while (N--) {
        getline(cin, a);
        int prev = alphabet[a[0]], ans = 0;
        for (int i = 1; i < a.length(); i++) {
            int curr = alphabet[a[i]];
            ans += min(abs(prev - curr), 28 - abs(prev - curr));
            prev = curr;
        }
        // (60 * PI) / (15 * 28) = PI / 7
        cout << setprecision(9) << (ans * M_PI / 7) + a.length() << "\n";
    }
    return 0;
}