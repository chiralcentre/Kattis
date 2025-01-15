#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef map<ll,int> mli;

string s; ll x; int Q;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    mli freq;
    ll total = 0, suitors = 0;
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> s >> x;
        if (s == "A") {
            freq[x]++;
            suitors++;
            total += x;
        } else {
            freq[x]--;
            if (freq[x] == 0) freq.erase(x);
            suitors--;
            total -= x;
        }
        if (suitors == 0) cout << "-1 -1 -1\n";
        else {
            ll f = (freq.begin())->first;
            ll s = (freq.rbegin())->first;
            double average = double(total) / double(suitors);
            cout << f << " " << s << " " << average << "\n";
        }
    }
    return 0;
}