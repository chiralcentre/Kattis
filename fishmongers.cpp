#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;
typedef pair<ll,ll> pll;
typedef vector<pll> vpll;

struct sort_snd_elem {
    bool operator() (const pll &left, const pll &right) {
        return left.second < right.second;
    }
};

int main() {
    int n,m; scanf("%d %d",&n,&m);
    vll w(n,0); vpll f;
    for (int i = 0; i < n; i++) scanf("%lld",&w[i]);
    sort(w.begin(), w.end());
    for (int i = 0; i < m; i++) {
        ll x,p; scanf("%lld %lld",&x,&p);
        f.emplace_back(x,p);
    }
    sort(f.begin(), f.end(), sort_snd_elem());
    ll profit = 0, i = n - 1, j = m - 1;
    while (i >= 0 && j >= 0) {
        pll pr = f[j--];
        int x = pr.first, p = pr.second;
        for (int k = 0; k < x && i >= 0; k++, i--) profit += p * w[i];
    }
    printf("%lld\n",profit);
    return 0;
}