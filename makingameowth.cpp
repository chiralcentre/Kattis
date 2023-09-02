#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N,P,X,Y;

int main() {
    scanf("%lld %lld %lld %lld",&N,&P,&X,&Y);
    printf("%lld\n", (P / (N - 1)) * (X * (N - 1) + Y) + (P % (N - 1)) * X);
    return 0;
}