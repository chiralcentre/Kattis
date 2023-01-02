#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    ll A,B; scanf("%lld %lld", &A, &B);
    ll r = A % B;
    printf("%lld\n",min(r,B - r));
    return 0;
}