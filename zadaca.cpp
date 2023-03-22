#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

ll MOD = 10000000000;

ll gcd(ll A, ll B) {
    while (B > 0) {
        ll rem = A % B;
        A = B;
        B = rem;
    }
    return A;
}

// find product of the N integers, and product of the M integers, and find gcd
int main() {
    int N; scanf("%d",&N);
    vll A(N,0);
    for (int i = 0; i < N; i++) scanf("%lld",&A[i]);
    int M; scanf("%d",&M);
    vll B(M,0);
    for (int i = 0; i < M; i++) scanf("%lld",&B[i]);
    ll ans = 1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            ll d = gcd(A[i], B[j]);
            if (d != 1) {
                ans *= d;
                ans %= MOD;
                A[i] /= d; B[j] /= d;
            }
        }
    }
    string a = to_string(ans);
    for (int i = max(0, (int) a.length() - 9); i < a.length(); i++) printf("%c", a[i]);
    printf("\n");
    return 0;
}