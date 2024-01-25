#include <bits/stdc++.h>

using namespace std;

int N;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    cout << "+" << string(N, '-') << "+" << "\n";
    for (int i = 0; i < N; i++) cout << "|" << string(N, ' ') << "|" << "\n";
    cout << "+" << string(N, '-') << "+" << "\n";
    return 0;
}