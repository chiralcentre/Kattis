#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

int main() {
    //score of each team can be taken as the sum of each player's row sums divided by 2
    //this is because we can always reorder the rows of the matrix such that the n/2 players in the strong team are the first n/2 rows in the matrix
    int n; scanf("%d",&n);
    vll rowSums(n,0);
    for (int i = 0; i < n; i++) {
        ll t = 0;
        for (int j = 0; j < n; j++) {
            ll a; scanf("%lld",&a);
            t += a;
        }
        rowSums[i] = t;
    }
    //sort rowSums and choose n/2 players with highest row sums as the strong team, and the other n/2 as the weak team
    sort(rowSums.begin(),rowSums.end());
    ll total = 0;
    for (int i = 0; i < n/2; i++) total -= rowSums[i];
    for (int i = n/2; i < n; i++) total += rowSums[i];
    printf("%lld\n",total / 2);
    return 0;
}