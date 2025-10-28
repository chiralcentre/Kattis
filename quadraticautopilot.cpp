#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll t0,e0,t1,e1,t2,e2;

// Equation 1: a * t0 ^ 2 + b * t0 + c = e0
// Equation 2: a * t1 ^ 2 + b * t1 + c = e1
// Equation 3: a * t2 ^ 2 + b * t2 + c = e2
// 2 - 1: a * (t1 ^ 2 - t0 * t0) + b * (t1 - t0) = e1 - e0
// 3 - 1: a * (t2 ^ 2 - t0 * t0) + b * (t2  - t0) = e2 - e0
int main() {
    scanf("%lld %lld\n%lld %lld\n%lld %lld",&t0,&e0,&t1,&e1,&t2,&e2);
    ll x1 = t1 * t1 - t0 * t0, y1 = t1 - t0, z1 = e1 - e0;
    ll x2 = t2 * t2 - t0 * t0, y2 = t2 - t0, z2 = e2 - e0;
    ll a = (y1 * z2 - z1 * y2) / (y1 * x2 - x1 * y2);
    ll b = (z1 - x1 * a) / y1;
    ll c = e1 - t1 * t1 * a - t1 * b;
    printf("%lld %lld %lld\n",a,b,c);
    return 0;
}