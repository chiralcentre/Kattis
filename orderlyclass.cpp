#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string A,B; cin >> A >> B;
    int s = 0, e = A.length() - 1;
    while (s < A.length() && A[s] == B[s]) s++;
    while (e >= 0 && A[e] == B[e]) e--;
    //guaranteed that A and B are not identical, so no runtime errors will occur where e < s
    string sA = A.substr(s, e - s + 1), sB = B.substr(s, e - s + 1);
    reverse(sA.begin(), sA.end());
    if (sA != sB) cout << 0 << "\n";
    else {
        int counter = 1;
        s--; e++;
        while (s >= 0 && e < A.length() && A[s] == A[e]) {s--; e++; counter++;}
        cout << counter << "\n";
    }
    return 0;
}