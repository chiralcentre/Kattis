#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n; ll m,k,typos[100000];

// algorithm runs in O(n) time
int main() {
    scanf("%d %lld %lld",&n,&m,&k);
    if (k < m) printf(":(\n");
    else {
        ll ans = 0, t = 0, e = k / m;
        for (int i = 0; i < n; i++) {
            scanf("%lld", &typos[i]);
            t += typos[i];
            if (t >= e) {
                ans += t / e;
                t %= e;
            }
        }
        if (t > 0) ans++;
        printf("%lld\n", ans);
    }
    return 0;
}