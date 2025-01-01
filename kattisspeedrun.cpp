#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll S,P,A,B;

int main() {
    scanf("%lld\n%lld\n%lld\n%lld",&S,&P,&A,&B);
    ll best = 1e12;
    // assume in optimal answer, Joshua solves extra x questions and creates y questions.
    // aim is to minimise Ax + By while ensuring that (S + x + y) / (P + y) > 0.5
    // range of y is 0 to P
    for (ll y = 0; y <= P; y++) {
        // find smallest value of x satisfying constraint -> 2x > P - 2S - y
        ll r = P - 2 * S - y;
        ll x = r / 2 + 1;
        ll t = ((S + y) * 2 > P + y) ? B * y : A * x + B * y;
        best = min(t, best);
    }
    printf("%lld\n",best);
    return 0;    
}