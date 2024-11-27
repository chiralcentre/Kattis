#include <bits/stdc++.h>
#include <iostream>
#include <sstream>
#include <set>

using namespace std;

typedef vector<string> vs;
typedef pair<int, string> pis;

int m; string w;

vs split_line_by_space(string sen) {
    stringstream ss(sen);
    string word;
    vs words;
    while (ss >> word) {
        words.push_back(word);
    }
    return words;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> m;
    cin.ignore();
    unordered_map<string,int> owed;
    for (int i = 0; i < m; i++) {
        getline(cin, w);
        vs line = split_line_by_space(w);
        string u = line[0], v = line[1];
        int d = stoi(line[2]);
        owed[u] -= d;
        owed[v] += d;
    }
    set<pis> unresolved;
    for (auto &[k,v]: owed) {
        if (v != 0) unresolved.insert(make_pair(v, k));
    }

    while (!unresolved.empty()) {
        pis L = *unresolved.begin();
        pis H = *unresolved.rbegin();
        int t = min(abs(L.first), H.first);
        unresolved.erase(L);
        unresolved.erase(H);
        int u1 = L.first + t;
        int v1 = H.first - t;
        if (u1 != 0) unresolved.insert(make_pair(u1, L.second));
        if (v1 != 0) unresolved.insert(make_pair(v1, H.second));
        cout << H.second << " " << L.second << " " << t << "\n";
    }
    cout << "settled" << "\n";
    return 0;
}