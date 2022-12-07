#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> trips, answer;
    set<int> unique;
    int total = 0;
    for (int i = 0; i < N; i++) {
        int x; cin >> x;
        trips.push_back(x);
        unique.insert(x);
        total += x;
    }
    for (int d: unique) answer.push_back(total - d);
    sort(answer.begin(),answer.end());
    cout << unique.size() << endl;
    for (int i = 0; i < unique.size(); i++) {
        cout << answer[i];
        if (i < unique.size() - 1) cout << " ";
    }
    cout << endl;
    return 0;
}