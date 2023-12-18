#include <bits/stdc++.h>

using namespace std;

int N;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    vector<string> friends(N,"");
    for (int i = 0; i < N; i++) cin >> friends[i];
    cout << friends[12 % N] << "\n";
    return 0;
}