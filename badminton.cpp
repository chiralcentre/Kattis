#include <bits/stdc++.h>

using namespace std;

int a,b,A = 0,B = 0;
char dash;
    
string solve(int a, int b) {
    if (a < 21 && b < 21) return "?";
    else if (a >= 21 && b < 21) {
        // A wins if a = 21 and b <= 19 or a = 22 and b = 20
        if ((a == 21 && b <= 19) || (a == 22 && b == 20)) return "A";
        if (a == 21 && b == 20) return "?";
        return "!";
    } else if (b >= 21 && a < 21) {
        // B wins if b = 21 and a <= 19 or b = 22 and a = 20
        if ((b == 21 && a <= 19) || (b == 22 && a == 20)) return "B";
        if (b == 21 && a == 20) return "?";
        return "!";
    } else { // a >= 21 and b >= 21
        if (a == 30 && b == 29) return "A";
        if (a == 29 && b == 30) return "B";
        if (a == 30 && b == 30) return "!";
        if (a - b == 2) return "A";
        if (b - a == 2) return "B";
        if (abs(a - b) < 2) return "?";
        return "!";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector<pair<int,int>> scores;

    while (cin >> a >> dash >> b) {
        scores.emplace_back(a, b);
    }
    // can only have at most 3 sets
    if (scores.size() > 3) {
        cout << "!";
        return 0;
    }
    for (int i = 0; i < scores.size(); i++) {
        a = scores[i].first, b = scores[i].second;
        string res = solve(a,b);
        if (res == "A") A++;
        else if (res == "B") B++;
        else if (res == "?") {
            if (i == scores.size() - 1) cout << "?";
            else cout << "!";
            return 0;
        } else {
            cout << "!";
            return 0;
        }
        // cannot have matches after a winner has been decided
        if (A == 2 || B == 2) {
            if (i != scores.size() - 1) {
                cout << "!";
                return 0;
            }
        }
    }
    if (A == 2) cout << "A";
    else if (B == 2) cout << "B";
    else cout << "?";
    return 0;
}
