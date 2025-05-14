#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll P,H,T;

int main() {
    scanf("%lld %lld %lld",&P,&H,&T);
    ll r = T - P - H;
    if (r < 0) printf("0\n"); 
    else {
        printf("%lld\n", 1 + (r / max(P, H)));
    }
    return 0;
}