#include <bits/stdc++.h>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false), cin.tie(NULL);
    string A,B; cin >> A >> B;
    cout << (A.length() >= B.length() ? "go\n" : "no\n");
    return 0;
}