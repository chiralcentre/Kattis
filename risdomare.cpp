#include <bits/stdc++.h>

using namespace std;

int N,A,S,pA,pS,idx;
string pref;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N >> pref;
    bool firstPref = (pref == "antal");
    pA = -1, pS = -1;
    for (int i = 1; i <= N; i++) {
        cin >> A >> S;
        if (A + S > pA + pS || A + S == pA + pS && ((A > pA && firstPref) || (S > pS && !firstPref))) {
            idx = i, pA = A, pS = S;
        }
    }
    cout << idx << "\n";
    return 0;
}