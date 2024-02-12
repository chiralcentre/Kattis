#include <bits/stdc++.h>

using namespace std;

int n;
double d,v,r,best = 10000;
string ship;

// fuel efficiency = distance / fuel consumed
// since distance is fixed, lower fuel consumed -> higher fuel efficiency
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> d;
    string winner;
    for (int i = 0; i < n; i++) {
        cin >> ship >> v >> r;
        if (r < best) {
            best = r;
            winner = ship;
        }
    }
    cout << winner << "\n";
    return 0;
}