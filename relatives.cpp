#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

bitset<10000010> bs;
vll p;
ll n;

//use sieve to get list of all primes up to upperbound in p
void sieve(ll upperbound) {
    ll size = upperbound + 1;
    bs.set(); // set all as 1s
    bs[0] = bs[1] = 0; // 0 and 1 are not primes
    for (ll i = 2; i < size; i++) {
        if (bs[i]) { // cross out multiples of i starting from i * i
            for (ll j = i * i; j < size; j += i) bs[j] = 0;
            p.push_back(i);
        }
    }
}

// EulerPhi totient function
ll EulerPhi(ll n) {
    ll ans = n;
    for (int i = 0; i < int(p.size()) && p[i] * p[i] <= n; i++) {
        if (n % p[i] == 0) ans -= ans / p[i]; // count unique
        while (n % p[i] == 0) n /= p[i]; 
    }
    if (n != 1) ans -= ans/n; //last factor
    return ans;
}

int main() {
    sieve(31630); // sqrt(10000000000) is approximately 31622.7766
    scanf("%lld",&n);
    while (n != 0) {
        printf("%lld\n", EulerPhi(n));
        scanf("%lld",&n);
    }
    return 0;
}