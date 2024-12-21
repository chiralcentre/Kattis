#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n; ll a,b,t = 0,m = 0;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld",&a,&b);
        t += b - a;
        m = max(t,m);
    }
    printf("%lld\n",m);
    return 0;
}