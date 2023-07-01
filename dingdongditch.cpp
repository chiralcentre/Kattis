#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

//total time complexity = O(N log N) + O(N) + O(Q)
int main() {
    int N,Q,B; scanf("%d %d",&N,&Q);
    vll A(N,0), ps(N,0);
    for (int i = 0; i < N; i++) scanf("%lld",&A[i]);
    sort(A.begin(), A.end());
    //compute prefix sums
    ps[0] = A[0];
    for (int i = 1; i < N; i++) ps[i] = ps[i - 1] + A[i];
    for (int i = 0; i < Q; i++) {
        scanf("%d",&B);
        printf("%lld\n",ps[B - 1]);
    }
    return 0;
}