#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll W,m,C;

int main() {
    scanf("%lld\n%lld\n%lld",&W,&m,&C);
    ll T = W * m * C;
    printf("%lld\n",T / 6000000 + (T % 6000000 > 0));
    return 0;
}