#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n,k;

// code runs in O(n) time
int main() {
    scanf("%lld %lld",&n,&k);
    int ans = 0; ll rem = 0;
    for (int i = 1; i <= n; i++) {
        int L = to_string(i).length();
        for (int j = 0; j < L; j++) rem *= 10;
        rem = (rem + i) % k;
        if (rem == 0) ans++;
    }
    printf("%d\n",ans);
    return 0;
}