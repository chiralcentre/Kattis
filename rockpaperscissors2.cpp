#include <bits/stdc++.h>

using namespace std;

string first,second;

unordered_map<string,string> win = {
    {"rock", "scissors"},
    {"paper", "rock"},
    {"scissors", "paper"}
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> first >> second;
    if (first == second) cout << "Draw\n";
    else if (win[first] == second) cout << "Player 1\n";
    else cout << "Player 2\n";
    return 0;
}