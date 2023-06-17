#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

// winnable if A % B == 0 or A >= 2B
// manually simulate if B < A < 2B
bool solve(ll A, ll B) {
    if (A % B == 0 || A / B >= 2) return true;
    return !solve(B, A - B);
}

int main() {
    ll N,M; scanf("%lld %lld",&N,&M);
    printf(solve(max(N,M), min(N,M)) ? "win\n" : "lose\n");
    return 0;
}