#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
//theorem: every number n > 11 can be expressed as the sum of two composite numbers
//proof - consider two cases, n is even and n is odd
//n is even -> note n - 4 is definitely even, and therefore n - 4 and 4 are two composite numbers summing up to n
//n is odd -> note n - 9 is definitely even, and therefore 9 and n - 9 are two composite numbers summing to n.
//handle numbers 2 to 11 manually
//note that 2,3,4,5,6,7,9,11 cannot be written as the sum of two composite numbers
//solutions for 8 and 10 are 8 = 4 + 4 and 10 = 4 + 6

void solve(ll N) {
    printf("2\n");
    if (N % 2) printf("%lld 9\n",N - 9);
    else printf("%lld 4\n", N - 4);
}

int main() {
    ll N; scanf("%lld",&N);
    solve(N);
    return 0;
}