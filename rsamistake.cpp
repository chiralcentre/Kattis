#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef long long ll;
typedef unordered_map<ll,int> umli;
typedef pair<umli,bool> hmb;

void debug(umli &hm) {
    for (auto pair: hm) {
        printf("key = %lld, value = %d\n",pair.first,pair.second);
    }
}

hmb primeFactor(ll n) {
    umli pf; bool prime = false;
    if (n == 2) prime = true;
    if (n % 2 == 0) pf[2] = 0;
    while (n % 2 == 0) {
        pf[2]++;
        n /= 2;
    }
    for (int i = 3; i < ll(sqrt(n)) + 1; i += 2) {
        if (n % i == 0) pf[i] = 0;
        while (n % i == 0) {
            pf[i]++;
            n /= i;
        }
    }
    // check if n is a prime number > 2
    if (n > 2) {
        if (pf.size() == 0) prime = true;
        pf[n] = 1;
    }
    return hmb(pf,prime);
}

//A and B share the same prime factor or A and B are divisible by a square -> no credit
//else, if A and B are distinct primes -> full credit
//else, if either A and B is not a prime -> partial credit
string solve(hmb &a, hmb &b, ll A, ll B) {
    umli pfA = a.first, pfB = b.first;
    bool primeA = a.second, primeB = b.second;
    //debug(pfA); debug(pfB);
    for (auto pair: pfA) {
        if (pfB.find(pair.first) != pfB.end() || pair.second >= 2) return "no credit";
    }
    for (auto pair: pfB) {
        if (pair.second >= 2) return "no credit";
    }
    return (primeA && primeB) ? "full credit": "partial credit";
}

//O(sqrt(N)) time complexity
int main() {
    ll A,B; scanf("%lld %lld",&A,&B);
    hmb a = primeFactor(A);
    hmb b = primeFactor(B);
    printf("%s\n",solve(a,b,A,B).c_str());
    return 0;
}