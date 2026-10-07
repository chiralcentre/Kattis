#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp> // Common file 
#include <ext/pb_ds/tree_policy.hpp> 
#include <functional> // for less 

using namespace __gnu_pbds;
using namespace std;

typedef long long ll;

typedef tree<ll, null_type,
    less<ll>, rb_tree_tag,
    tree_order_statistics_node_update> ordered_set;

int n; ll b,a,total = 0;
double m;

int main() {
    scanf("%d",&n);
    vector<ll> nums;
    ordered_set S;
    for (int i = 0; i < n; i++) {
        scanf("%lld",&b);
        nums.push_back(b);
        S.insert(b);
        total += b;
    }
    scanf("%lld %lf",&a,&m);
    // find all possible pairs that can be removed, there are at most n / 2 pairs
    // sum of pair to be removed = 2 * A - a*n + 2 * a, where A is the average of the original list
    // for each pair to be removed, check if median indeed changes by given amount after removing the pair in O(log n) time
    // overall time complexity is O(n log n)
    // sort nums vector in O(n log n) time for two pointer approach
    sort(nums.begin(), nums.end());
    ll M = (ll) (m * 2); // this works as m is always a whole number or 0.5 off whole number
    // m1 is 2 times of the actual median of original list
    ll m1 = (n % 2 == 1) ? 2 * (*S.find_by_order(n / 2)): (*S.find_by_order(n / 2 - 1)) + (*S.find_by_order(n / 2));
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
            S.erase(nums[L]);
            S.erase(nums[R]);
            // parity of total number of elements is preserved after removing 2 elements
            ll m2 = (n % 2 == 1) ? 2 * (*S.find_by_order(n / 2 - 1)): (*S.find_by_order(n / 2 - 2)) + (*S.find_by_order(n / 2 - 1));
            if (m1 + M == m2) printf("%lld %lld\n",nums[L],nums[R]);
            S.insert(nums[L]);
            S.insert(nums[R]);
            L++;
            R--;
        }
    }
    return 0;
}