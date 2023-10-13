#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N,K,H;

// O(N) approach
int main() {
    ll N,K; scanf("%lld %lld",&N,&K); 
    vector<ll> houses;
    houses.push_back(0);
    ll safetyRating = N * (N + 1) / 2;
    for (ll i = 0; i < K; i++) {
        scanf("%lld",&H);
        houses.push_back(H);
    }
    houses.push_back(N + 1);
    // find number of houses on consecutive stretches of unsafe houses, g, and substract g * (g + 1) / 2 from total
    for (ll i = 1; i <= K + 1; i++) {
        ll g = houses[i] - houses[i - 1] - 1;
        safetyRating -= (g * (g + 1)) >> 1;
    }
    printf("%lld\n",safetyRating);
    return 0;
}