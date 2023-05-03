#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s; cin >> s;
    if (s.size() < 4) {// up to 6! 
        int ans = 1, n = stoi(s);
        for (int i = 1; i < 7; i++) {
            ans *= i;
            if (ans == n) {
                cout << i << "\n";
                break;
            }
        }
    } else {
        //log(ab) = log(a) + log(b)
        //number of digits in a number n = floor(log10(n)) + 1
        double d = 0.0;
        for (int i = 1; i <= 1000000; i++) {
            d += log10(i);
            if (floor(d) + 1 == s.size()) {
                cout << i << "\n";
                break;
            }
        }
    }
    return 0;
}