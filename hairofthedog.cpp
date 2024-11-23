#include <bits/stdc++.h>

using namespace std;

int N,hungover = 0;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    vector<string> days(N, "");
    for (int i = 0; i < N; i++) cin >> days[i];
    for (int i = 1; i < N - 1; i++) {
        if (days[i] == "drunk" && days[i + 1] == "sober") hungover++;
    }
    cout << hungover << "\n";
    return 0;
}