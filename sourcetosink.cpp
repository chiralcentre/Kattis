#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll L,W,V;

// let a be the valve connecting to bottom reservoir and b be valve connecting to general water system
// to send v m^3 over, a needs to open, a needs to close, b needs to open, b needs to close
int main() {
    scanf("%lld %lld %lld",&L,&W,&V);
    ll v = L * W;
    printf("%lld\n", ((v / V + (v % V > 0)) << 2) - 1);
    return 0;
}