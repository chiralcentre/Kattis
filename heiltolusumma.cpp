#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N;

int main() {
    scanf("%lld",&N);
    if (N >= 1) printf("%lld\n",(N * (N + 1)) / 2);
    else if (N == 0) printf("1\n");
    else printf("%lld\n",((N + 1) * (2 - N)) / 2);
    return 0;
}