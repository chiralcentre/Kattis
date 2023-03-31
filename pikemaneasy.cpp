#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

int main() {
    ll N,T,A,B,C,t0; 
    scanf("%lld %lld",&N,&T);
    scanf("%lld %lld %lld %lld",&A,&B,&C,&t0);
    vll t(N,0); t[0] = t0;
    for (int i = 1; i < N; i++) t[i] = ((A * t[i - 1] + B) % C) + 1;
    sort(t.begin(),t.end());
    ll counter = 0, p = 0, penalty = 0;
    for (int i = 0; i < N; i++) {
        if (counter + t[i] <= T) {
            counter += t[i];
            p++; 
            penalty = (penalty + counter) % (1000000007);
        } else break;
    }
    printf("%lld %lld\n", p, penalty);
    return 0;
}