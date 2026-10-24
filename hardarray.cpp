#include <bits/stdc++.h>
using namespace std;
using ll = long long;

static char ibuf[1 << 16];
static int ipos = 0, ilen = 0;

static inline int gc() {
    if (ipos == ilen) {
        ilen = (int)fread(ibuf, 1, sizeof(ibuf), stdin);
        ipos = 0;
        if (ilen <= 0) return -1;
    }
    return ibuf[ipos++];
}

static inline ll readInt() {
    int c = gc();
    while (c != '-' && (c < '0' || c > '9')) c = gc();
    bool neg = false;
    if (c == '-') { neg = true; c = gc(); }
    ll x = 0;
    while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = gc(); }
    return neg ? -x : x;
}

// smallest s >= 0 with s*s >= v
static inline ll ceilSqrt(ll v) {
    if (v <= 0) return 0;
    ll s = (ll)sqrtl((long double)v);
    while (s > 0 && (s - 1) * (s - 1) >= v) --s;
    while (s * s < v) ++s;
    return s;
}

int main() {
    int n = (int)readInt();
    vector<ll> A(n + 1), B(n + 1);
    vector<pair<ll, ll>> pts(n + 1);   // (x, y)

    pts[0] = {0, 0};                   // the L = 1 endpoint
    for (int i = 1; i <= n; i++) { A[i] = readInt(); pts[i].first  = pts[i - 1].first  + A[i]; }
    for (int i = 1; i <= n; i++) { B[i] = readInt(); pts[i].second = pts[i - 1].second + B[i]; }

    // seed from adjacent pairs: valid bound, keeps r small enough that no square overflows
    ll best = LLONG_MAX;
    for (int i = 1; i <= n; i++) best = min(best, A[i] * A[i] + B[i] * B[i]);

    sort(pts.begin(), pts.end());

    multiset<pair<ll, ll>> S;          // (y, x) of live candidates
    int l = 0;
    for (int j = 0; j <= n && best > 0; j++) {
        ll r = ceilSqrt(best);
        ll xj = pts[j].first, yj = pts[j].second;

        while (l < j && xj - pts[l].first > r) {
            S.erase(S.find({pts[l].second, pts[l].first}));
            l++;
        }

        auto it = S.lower_bound({yj - r, LLONG_MIN});
        for (; it != S.end() && it->first <= yj + r; ++it) {
            ll dx = xj - it->second, dy = yj - it->first;
            ll d = dx * dx + dy * dy;
            if (d < best) best = d;
        }

        S.insert({yj, xj});
    }

    printf("%lld\n", best);
    return 0;
}