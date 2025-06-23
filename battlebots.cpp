#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n;

int main() {
    scanf("%lld",&n);
    ll p = ll(ceil(log(n) / log(2)));
    ll a = ll(pow(2, p));
    ll b = a / 2;
     // account for floating point imprecision
    if (b >= n) p--;
    if (a < n) p++;
    printf("%lld\n", p + 1);
    return 0;
}