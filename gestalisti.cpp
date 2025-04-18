#include <bits/stdc++.h>

using namespace std;

int N;
string op, name;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    unordered_set<string> guestList;
    for (int i = 0; i < N; i++) {
        cin >> op >> name;
        if (op == "+") guestList.insert(name);
        else if (op == "-") guestList.erase(name);
        else cout << (guestList.find(name) == guestList.end() ? "Neibb\n" : "Jebb\n"); 
    }
    return 0;
}