#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll n,b;

int main() {
    scanf("%lld %lld",&n,&b);
    printf("%lld\n",ll(floor(log(double(n)) / log(double(b + 1)))) + 1);
    return 0;
}