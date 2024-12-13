#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll p,a,t = 0,same_origin_pairs = 0; int n;

int main() {
    scanf("%d %lld",&n,&p);
    for (int i = 0; i < n; i++) {
        scanf("%lld",&a);
        t += a;
        same_origin_pairs += (a * (a - 1)) >> 1;
    }
    ll total = ((t * (t - 1)) >> 1) - same_origin_pairs;
    printf("%lld\n",total / p + (total % p > 0));
    return 0;
}