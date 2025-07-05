#include <bits/stdc++.h>
using namespace std;

int N, K;
vector<vector<int>> courses_list;
vector<vector<int>> memo;

int dp(int i, int r) {
    if (i == (int)courses_list.size() || r == 0)
        return 0;
    if (memo[i][r] != -1)
        return memo[i][r];

    int chosen = 0;
    for (int d : courses_list[i]) {
        if (d <= r) {
            int res = dp(i + 1, r - d) + d;
            if (res == K) {
                memo[i][r] = K;
                return K;
            }
            chosen = max(chosen, res);
        }
    }

    int not_chosen = dp(i + 1, r);
    if (not_chosen == K) {
        memo[i][r] = K;
        return K;
    }

    memo[i][r] = max(chosen, not_chosen);
    return memo[i][r];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;
    unordered_map<string, unordered_set<int>> courses;

    for (int i = 0; i < N; ++i) {
        int d; string s;
        cin >> d >> s;
        courses[s].insert(d);
    }

    // Move from map to vector
    for (auto& [_, lst] : courses) {
        vector<int> v(lst.begin(), lst.end());
        courses_list.push_back(move(v));
    }

    memo.assign((int)courses_list.size(), vector<int>(K + 1, -1));
    cout << dp(0, K) << "\n";

    return 0;
}