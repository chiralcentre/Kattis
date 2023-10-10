#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll Q,M,S,L;

bool verify(int N) {
    ll num = N / Q;
    if (num * M < L) return false; // check if all L slots are taken up
    return M * N >= Q * L + S; // check if all L + S slots can be fulfilled with timing of N seconds
}

// conduct binary search, total time complexity is O(n log (S + L * Q))
int main() {
    scanf("%lld %lld %lld %lld",&Q,&M,&S,&L);
    ll LOW = 0, HIGH = S + L * Q, ans = -1;
    while (LOW <= HIGH) {
        ll m = LOW + ((HIGH - LOW) >> 1);
        // printf("LOW = %lld, HIGH = %lld, m = %lld\n",LOW,HIGH,m);
        if (verify(m)) {
            ans = m;
            HIGH = m - 1;
        } else LOW = m + 1;
    }
    printf("%lld\n",ans);
    return 0;
}