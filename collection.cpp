#include <bits/stdc++.h>
using namespace std;

static const int MAXN = 100005;
int lc[MAXN], rc[MAXN], sz[MAXN];
unsigned pri[MAXN];

static inline void upd(int v) { sz[v] = sz[lc[v]] + sz[rc[v]] + 1; }

// a gets keys <= k, b gets keys > k.  (node index == key)
void split(int v, int k, int &a, int &b) {
    if (!v) { a = b = 0; return; }
    if (v <= k) { a = v; split(rc[v], k, rc[a], b); upd(a); }
    else        { b = v; split(lc[v], k, a, lc[b]); upd(b); }
}

// requires every key in a < every key in b
int mergeT(int a, int b) {
    if (!a) return b;
    if (!b) return a;
    if (pri[a] > pri[b]) { rc[a] = mergeT(rc[a], b); upd(a); return a; }
    lc[b] = mergeT(a, lc[b]); upd(b); return b;
}

static inline int minKey(int v) { while (lc[v]) v = lc[v]; return v; }
static inline int maxKey(int v) { while (rc[v]) v = rc[v]; return v; }

int kth(int v, int k) {                 // 1-indexed
    while (true) {
        int l = sz[lc[v]];
        if (k == l + 1) return v;
        if (k <= l) v = lc[v];
        else { k -= l + 1; v = rc[v]; }
    }
}

// block-peeling union; O(b log N) for b interleaved blocks
int unite(int A, int B) {
    if (!A) return B;
    if (!B) return A;
    if (maxKey(A) < minKey(B)) return mergeT(A, B);
    if (maxKey(B) < minKey(A)) return mergeT(B, A);
    int out = 0;
    while (A && B) {
        if (minKey(A) > minKey(B)) swap(A, B);
        int k = minKey(B), blk, rest;
        split(A, k - 1, blk, rest);
        out = mergeT(out, blk);
        A = rest;
        swap(A, B);
    }
    if (A) out = mergeT(out, A);
    if (B) out = mergeT(out, B);
    return out;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;

    mt19937 rng(998244353);
    vector<int> root(n + 1);
    for (int v = 1; v <= n; v++) {
        lc[v] = rc[v] = 0; sz[v] = 1; pri[v] = rng();
        root[v] = v;                       // playlist v holds record v
    }

    vector<int> tagStack;
    tagStack.reserve(q);

    for (int Q = 0; Q < q; Q++) {
        int t, i, j;
        cin >> t >> i >> j;
        if (t == 1) {
            cout << kth(root[i], j) << '\n';
        } else if (t == 2) {
            root[i] = unite(root[i], root[j]);
            root[j] = 0;
            tagStack.push_back(j);
        } else {
            int tag = tagStack.back(); tagStack.pop_back();
            int key = kth(root[i], j);     // j-th smallest stays
            int l, r;
            split(root[i], key, l, r);
            root[i] = l;
            root[tag] = r;
        }
    }
    return 0;
}