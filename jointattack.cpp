#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

int n;

int main() {
    scanf("%d",&n);
    vll coeff(n, 0);
    for (int i = 0; i < n; i++) scanf("%lld",&coeff[i]);
    ll numerator = 1, denominator = coeff[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        numerator = coeff[i] * denominator + numerator;
        if (i > 0) swap(numerator, denominator);
    }   
    printf("%lld/%lld\n",numerator,denominator);
    return 0;
}