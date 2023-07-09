#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

bitset<10000> bs;
vi p; int npf[2000001],Q,n;

//use sieve to get list of all primes up to upperbound in p
void sieve(int upperbound) {
    int size = upperbound + 1;
    bs.set(); // set all as 1s
    bs[0] = bs[1] = 0; // 0 and 1 are not primes
    for (int i = 2; i < size; i++) {
        if (bs[i]) { // cross out multiples of i starting from i * i
            for (int j = i * i; j < size; j += i) bs[j] = 0;
            p.push_back(i);
        }
    }
}

int solve(int N) {
    int numDiv = 1, numPF = 0;
    for (int i = 0; i < int(p.size()) && p[i] * p[i] <= N; i++) {
        int power = 0;
        if (N % p[i] == 0) numPF++;
        while (N % p[i] == 0) {N /= p[i]; ++power;}
        numDiv *= power + 1;
    }
    if (N != 1) {numDiv <<= 1; numPF++;}
    return numDiv - numPF;
}

int main() {
    sieve(1420); // sqrt(2000000) ~= 1414
    scanf("%d", &Q);
    for (int i = 2; i <= 2000000; i++) npf[i] = solve(i);
    while (Q--) {
        scanf("%d", &n);
        printf("%d\n", npf[n]);
    }
    return 0;
}