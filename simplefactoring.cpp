#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

//expression is factorable only if discriminant is positive and perfect square
int main() {
    int n; scanf("%d",&n);
    while (n--) {
        ll a,b,c; scanf("%lld %lld %lld",&a,&b,&c);
        ll d = b * b - 4 * a * c;
        if (d < 0) printf("NO\n");
        else {
            ll root = ll(sqrt(d));
            (root * root == d) ? printf("YES\n") : printf("NO\n");
        }
    }
    return 0;
}