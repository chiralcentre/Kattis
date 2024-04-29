#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

double d; ll k;
int main() {
    scanf("%lf\n%lld",&d,&k);
    double ans = d;
    // after 17 iterations, desired accuracy is attained
    for (ll i = 0; i < min(17ll, k); i++) {
        d *= 0.5;
        ans += d;
    }
    printf("%lf\n",ans);
    return 0;
}