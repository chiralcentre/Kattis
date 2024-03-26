#include <bits/stdc++.h>

using namespace std;

int n; string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    bool a = false, b = false;
    for (int i = 0; i < n; i++) {
        cin >> s;
        if (s == "nautakjot") a = true;
        if (s == "kjuklingur") b = true;
        if (a && b) {
            cout << "blandad best\n";
            return 0;
        }
    }
    cout << (a ? "nautakjot\n" : "kjuklingur\n");
    return 0;
}