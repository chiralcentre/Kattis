#include <bits/stdc++.h>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string N,M;
    cin >> N >> M;
    int idx = N.length() - M.length();
    if (idx < 0) {
        cout << "0.";
        for (int i = 0; i < abs(idx) - 1; i++) cout << "0";
        int end = 0;
        for (int i = 0; i < N.length(); i++)  {
            if (N[i] != '0') end = i;
        }
        for (int i = 0; i < end + 1; i++) cout << N[i];
    } else {
        for (int i = 0; i < idx + 1; i++) cout << N[i];
        int end = 0;
        for (int i = idx + 1; i < N.length(); i++)  {
            if (N[i] != '0') end = i;
        }
        if (end != 0) {
            cout << ".";
            for (int i = idx + 1; i < end + 1; i++) cout << N[i];
        }
    }
    cout << "\n";
    return 0;
}