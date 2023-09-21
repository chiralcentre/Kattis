#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unordered_map<ll,ll> umll;


ll N,p,Q,x,y; string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    umll prices;
    ll total = 0;
    for (int i = 0; i < N; i++) {
        cin >> p;
        prices[p]++;
        total += p;
    }
    ll increment = 0;
    cin >> Q;
    while (Q--) {
        cin >> s;
        if (s == "INFLATION") {
            cin >> x;
            increment += x;
            total += x * N;
        } else if (s == "SET") {
            cin >> x >> y;
            if (prices.find(x - increment) != prices.end()) {
                ll quantity = prices[x - increment];
                prices.erase(x - increment);
                prices[y - increment] += quantity;
                total += quantity * (y - x);
            }
        }
        cout << total << "\n";
    }
    return 0;
}