#include <bits/stdc++.h>
#include <string>

using namespace std;

//find length of longest common prefix of two strings
int LCP(string s1, string s2) {
    int counter = 0;
    for (int i = 0; i < min(s1.length(), s2.length()); i++) {
        if (s1[i] == s2[i]) counter++;
        else return counter;
    }
    return counter;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s1,s2; cin >> s1 >> s2;
    cout << s1.length() + s2.length() - 2 * LCP(s1,s2) << "\n";
    return 0;
}