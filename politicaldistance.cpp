#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll xp,yp,xv,yv;

int main() {
    scanf("%lld %lld\n%lld %lld",&xp,&yp,&xv,&yv);
    printf("%lld\n",(xp - xv) * (xp - xv) + (yp - yv) * (yp - yv));
    return 0;
}