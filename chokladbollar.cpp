#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N,B,S;

int main() {
    scanf("%lld%lld %lld",&N,&B,&S);
    ll T = B + S;
    // N - R bags with A balls
    // R bags with A + 1 balls
    ll A = T / N, R = T % N, keep = 0;
    // keep track of balls to keep
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            ll k = i + j; // number of bags among the 2 at A + 1
            if (k > R || (k == 0 && R == N - 1)) continue;
            keep = max(keep, min(B, A + i) + min(S, A + j));
        }
    }
    printf("%lld\n", T - keep);
    return 0;
}