#include <bits/stdc++.h>

using namespace std;

unordered_map<string,int> freq;

int n,m,k; string s;

bool comparator(const pair<string,int> &p1,const pair<string,int> &p2){
    if (p1.second == p2.second) { // If numbers are same, sort by string
        return p1.first < p2.first;
    }
    return p1.second > p2.second; // Descending order
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;
        freq[s] = 0;
    }
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> k;
        for (int j = 0; j < k; j++) {
            cin >> s;
            freq[s]++;
        }
    }
    vector<pair<string,int>> students(freq.begin(), freq.end());
    sort(students.begin(), students.end(), comparator);
    for (auto& p: students) cout << p.second << " " << p.first << "\n";
    return 0;
}