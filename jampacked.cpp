#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n,k;

int main() {
    scanf("%lld %lld",&n,&k);
    if (k >= n) printf("%lld\n",n);
    else {
        ll b = n / k + (n % k > 0);
        printf("%lld\n", n / b);
    }
    return 0;
}