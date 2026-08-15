#include <bits/stdc++.h>

using namespace std;

string s;

string solve(string s) {
    int n = s.length();
    for (int i = 0; i < n / 2; i++) {
        if (s[i] != s[n - i - 1]) {
            return "Nothing special about this string :(\n";
        }
    }
    return "Palindrome!";
}

int main() {
    cin >> s;
    cout << solve(s);
    return 0;
}