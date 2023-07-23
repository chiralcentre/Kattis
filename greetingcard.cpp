#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unordered_map<ll,ll> umll;
typedef pair<ll,ll> pll;

umll points; ll n,a,b;

ll mask = 2147483647;

// there are only 12 possible points to look at
ll x[12] = {0, 0, 2018, -2018, 
            1118, -1118, 1118, -1118,
            1680, -1680, 1680, -1680};
ll y[12] = {2018, -2018, 0, 0,
            1680, 1680, -1680, -1680,
            1118, 1118, -1118, -1118};

// compress the 2D coordinates into a 1D coordinate
ll encode(ll a, ll b) {return (a << 31) + b;}
pll decode(ll c) {return make_pair(c >> 31, c & mask);}

int main() {
    scanf("%lld",&n);
    for (ll i = 0; i < n; i++) {
        scanf("%lld %lld",&a,&b);
        ll h = encode(a,b);
        if (points.find(h) == points.end()) points[h] = 1;
        else points[h]++;
    }
    ll ans = 0;
    for (auto &[k,p]: points) {
        pll pr = decode(k);
        ll u = pr.first, v = pr.second;
        for (int i = 0; i < 12; i++) {
            if (u + x[i] >= 0 && v + y[i] >= 0) {
                ll h = encode(u + x[i], v + y[i]);
                if (points.find(h) != points.end()) ans += p * points[h];
            }
        }
    }
    printf("%lld\n", ans >> 1); // divide by 2 to account for duplicates
}