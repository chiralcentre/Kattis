#include <bits/stdc++.h>

using namespace std;

int n,k,a;
string res = "fyrst", prefix = "";

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a == k) {
            if (i == 1) {
                prefix = "naest";
            } else if (i > 1) {
                prefix = to_string(i + 1) + " ";
            }
            cout << prefix << res << "\n";
            break;
        }
    }
    return 0;
}