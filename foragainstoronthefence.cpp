#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll xp,yp,xv,yv,u;

int main() {
    scanf("%lld %lld\n%lld %lld\n%lld",&xp,&yp,&xv,&yv,&u);
    ll d = (xp - xv) * (xp - xv) + (yp - yv) * (yp - yv);
    if (d < u) printf("for\n");
    else if (d == u) printf("on the fence\n");
    else printf("against\n");
    return 0;
}