#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;

ll K,a,b;

int main() {
    scanf("%lld\n%lld\n%lld",&K,&a,&b);
    vector<pll> ans;
    for (int i = 0; i <= K / a; i++) {
        ll rem = K - i * a;
        if (rem % b == 0) ans.push_back(make_pair(i, (rem / b)));
    }
    printf("%d\n",ans.size());
    for (auto [a,b]: ans) printf("%lld %lld\n",a,b);
    return 0;
}