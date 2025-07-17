#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
ll T,N,K;

int main() {
    scanf("%lld",&T);
    for (int i = 0; i < T; i++) {
        scanf("%lld %lld",&N,&K);
        bool works = true;
        for (int j = 0; j < N; j++) {
            if (K % 2 == 0) works = false;
            K /= 2;
        }
        works ? printf("Case #%d: ON\n", i + 1) : printf("Case #%d: OFF\n", i + 1);
    }
    return 0;
}