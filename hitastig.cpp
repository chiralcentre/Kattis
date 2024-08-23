#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n; ll a,highest,lowest;

int main() {
    scanf("%d",&n);
    scanf("%lld",&a);
    highest = a; lowest = a;
    for (int i = 1; i < n; i++) {
        scanf("%lld",&a);
        highest = max(a, highest);
        lowest = min(a, lowest);
    }
    printf("%lld %lld",highest,lowest);
    return 0;
}