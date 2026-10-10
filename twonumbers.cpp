#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n; ll b,a,total = 0;
double m;

int main() {
    scanf("%d",&n);
    vector<ll> nums;
    for (int i = 0; i < n; i++) {
        scanf("%lld",&b);
        nums.push_back(b);
        total += b;
    }
    scanf("%lld %lf",&a,&m);
    // find all possible pairs that can be removed, there are at most n / 2 pairs
    // sum of pair to be removed = 2 * A - a*n + 2 * a, where A is the average of the original list
    // for each pair to be removed, check if median indeed changes by given amount after removing the pair in O(1) time
    // overall time complexity is O(n log n)
    // sort nums vector in O(n log n) time for two pointer approach
    sort(nums.begin(), nums.end());
    // at(k, i, j) = element at index k of the sorted array after deleting sorted positions i < j
    auto at = [&](int k, int i, int j) -> ll {
        if (k < i)     return nums[k];
        if (k <= j - 2) return nums[k + 1];
        return nums[k + 2];
    };
    ll M = (ll) (m * 2); // this works as m is always a whole number or 0.5 off whole number
    // m1 is 2 times of the actual median of original list
    ll m1 = (n % 2 == 1) ? 2 * nums[n / 2]: nums[n / 2 - 1] + nums[n / 2];
    int L = 0, R = n - 1;
    ll A = total / n; // guaranteed to be integer by question constraints
    ll T = 2 * A - a * n + 2 * a;
    while (L < R) {
        ll t = nums[L] + nums[R];
        if (t < T) {
            L++;
        } else if (t > T) {
            R--;
        } else {
            ll m2 = (n % 2 == 1) ? 2 * at(n / 2 - 1, L, R): at(n / 2 - 2, L, R) + at(n / 2 - 1, L, R);
            if (m1 + M == m2) printf("%lld %lld\n",nums[L],nums[R]);
            L++;
            R--;
        }
    }
    return 0;
}