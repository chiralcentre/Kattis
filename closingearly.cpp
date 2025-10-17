#include <bits/stdc++.h>

typedef long long ll;

ll R,S,N,A,total = 0;

int main() {
    scanf("%lld %lld %lld",&R,&S,&N);
    for (ll i = 0; i < N; i++) {
        if (total % S == R) {
            printf("%lld\n", i);
            return 0;
        }
        scanf("%lld",&A);
        total += A;
    }
    if (total % S == R) {
        printf("%lld\n", N);
    } else {
        printf("-1\n");
    }
    return 0;
}