#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    const ll upperBound = 1000000000;
    ll N; cin >> N;
    vll fib(2,1);
    while (fib.back() < upperBound) fib.push_back(fib[fib.size() - 2] + fib.back());
    // there are only 44 fibonacci numbers < 10^9, so naive iteration works
    vll ans;
    while (N != 0) {
        for (int i = fib.size() - 1; i > 0; i--) {
            if (fib[i] <= N) {
                N -= fib[i];
                ans.push_back(fib[i]);
                break;
            }
        }
    }
    for (int i = ans.size() - 1; i >= 0; i--) {
        cout << ans[i];
        if (i > 0) cout << " ";
    }
    return 0;
}
