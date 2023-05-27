#include <bits/stdc++.h>

using namespace std;

typedef vector<char> vc;

void printRes(vc &res) {
    if (res.empty()) cout << "YODA\n";
    else {
        string s = "";
        for (int i = res.size() - 1; i >= 0; i--) s += res[i];
        cout << stoi(s) << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string N,M; cin >> N >> M;
    vc A,B;
    int i = N.length() - 1, j = M.length() - 1;
    while (i >= 0 && j >= 0) {
        int a = N[i] - '0', b = M[j] - '0';
        if (a > b) A.push_back(N[i]);
        else if (a < b) B.push_back(M[j]);
        else {
            A.push_back(N[i]);
            B.push_back(M[j]);
        }
        i--; j--;
    }
    while (i >= 0) A.push_back(N[i--]);
    while (j >= 0) B.push_back(M[j--]);
    printRes(A);
    printRes(B);
    return 0;
}