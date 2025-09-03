#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll C;

ll digit_sum(ll C) {
    ll ds = 0;
    while (C > 0) {
        ds += C % 10;
        C /= 10;
    }
    return (ds > 9) ? digit_sum(ds) : ds;
}

int main() {
    scanf("%lld",&C);
    printf("%lld\n",digit_sum(C));
    return 0;
}