#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll N; cin >> N;
    vector<ll> ans;
    for (ll i = 1; i <= sqrt(N); i++) {
        if (N % i == 0) {
            if (i * i != N) ans.push_back(N / i);
            cout << i << "\n";
        }
    }
    for (int i = ans.size() - 1; i >= 0; i--) cout << ans[i] << "\n";
    return 0;
}