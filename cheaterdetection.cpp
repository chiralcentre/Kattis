#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int N; ll a,b;

int main() {
    scanf("%d",&N);
    for (int i = 0; i < N; i++) {
        scanf("%lld.%lld",&a,&b);
        // multiply original number by 1000 to avoid FPE
        ll res = (a * 100 + b) * 10;
        ll m = res / 15;
        ll L = m * 15, H = L + 15;
        // round down
        L = L - L % 10; H = H - H % 10;
        (L != res && H != res) ? printf("IMPOSSIBLE\n") : printf("VALID\n");
    }
    return 0;
}