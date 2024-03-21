#include <bits/stdc++.h>

using namespace std;

string s;

int main() {
    cin >> s;
    int counter = 0;
    for (char c: s) {
        int a  = int(c);
        if ((65 <= a && a <= 90) || (97 <= a && a <= 122)) counter++;
    }
    cout << counter;
    return 0;
}