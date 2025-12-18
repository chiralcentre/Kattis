#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef vector<ll> vll;

int n; ll k,m;

int main() {
    scanf("%d",&n);
    vll weights(n, 0), reps(n, 0);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld %lld",&k,&m,&weights[i]);
        reps[i] = k * m;
    }
    sort(weights.begin(), weights.end());
    sort(reps.begin(), reps.end());
    ll load = 0;
    for (int i = 0; i < n; i++) load += weights[i] * reps[i];
    printf("%lld\n",load);
    return 0;
}