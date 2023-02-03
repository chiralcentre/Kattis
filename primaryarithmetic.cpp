#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string A,B;
    while (true) {
        cin >> A >> B;
        if (A == "0" && B == "0") break;
        int d = abs((int) A.length() - (int) B.length());
        if (A.length() > B.length()) {
            for (int i = 0; i < d; i++) B = "0" + B;
        } else if (B.length() > A.length()) {
            for (int i = 0; i < d; i++) A = "0" + A;    
        }
        int carry = 0, prev = 0;
        for (int i = A.length() - 1; i >= 0; i--) {
            int t =  A[i] + B[i] - 2 * '0' + prev;
            if (t >= 10) {carry++; prev = 1;}
            else prev = 0;
        }
        string ans = (carry == 0 ? "No" : to_string(carry));
        string end = (carry == 0 || carry == 1 ? "operation." : "operations.");
        cout << ans << " carry " << end << "\n";
    }
    return 0;
}