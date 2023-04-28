#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    ll k,m,n; scanf("%lld %lld %lld",&k,&m,&n);
    ll r = k % (m + n);
    printf(r >= m ? "Alex\n" : "Barb\n");
    return 0;
}