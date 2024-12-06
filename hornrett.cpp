#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll a,b,c;

int main() {
    scanf("%lld %lld %lld",&a,&b,&c);
    // right angled triangles have integer area
    (a * a + b * b == c * c) ? printf("%lld\n", (a * b) >> 1) : printf("-1\n");
    return 0;
}