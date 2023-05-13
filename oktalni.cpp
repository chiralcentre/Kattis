#include <bits/stdc++.h>

using namespace std;

unordered_map<string,int> binOct = {{"000", 0}, {"001", 1}, {"010", 2}, {"011", 3},
                                    {"100", 4}, {"101", 5}, {"110", 6}, {"111", 7}};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string n; cin >> n;
    vector<int> octal;
    int i = n.length() - 1;
    while (i >= 2) {
        string s = n.substr(i - 2, 3);
        octal.push_back(binOct[s]);
        i -= 3;
    }
    if (i != -1) {
        string r = n.substr(0,i + 1);
        int l = r.length();
        //padding
        for (int j = 0; j < 3 - l; j++) r = "0" + r;
        octal.push_back(binOct[r]);
    }
    for (int j = octal.size() - 1; j >= 0; j--) cout << octal[j];
    cout << "\n";
    return 0;
}