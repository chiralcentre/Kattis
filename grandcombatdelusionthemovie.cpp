#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
 
// Smallest damage D such that Matt survives all enemies with health h
// Function runs in O(m) time with a constant factor of log(1e9)
ll damageNeeded(ll h, const vector<ll>& enemies) {
    // damage taken by Matt by enemy is ceil(h_i / D) - 1, where D is his damage,h_i is health of i_th enemy
    // set L = 1, H = 1e9, since maximum enemy health is 1e9
    ll L = 1, H = 1e9, ans = 0;
    while (L <= H) {
        ll M = L + ((H - L) >> 1);
        ll total_dmg_taken = 0;
        for (ll x: enemies) total_dmg_taken += (x + M - 1) / M - 1;
        if (total_dmg_taken >= h) L = M + 1;
        else {
            ans = M;
            H = M - 1;
        }
    }
    return ans;
}
 
// Minimum contiguous subarray sum (empty = 0 allowed) that is >= target.
// Function runs in O(n log n)
ll cheapestAtLeast(const vector<ll>& c, ll target) {
    // prefix sums + predecessor query (std::set upper_bound)
    vector<ll> prefixSums(c.size(), 0);
    prefixSums[0] = c[0];
    for (int i = 1; i < prefixSums.size(); i++) prefixSums[i] = prefixSums[i - 1] + c[i];
    // for subarray [L,R] inclusive, prefixSums[R] - prefixSums[L - 1] = sum of subarray [L,R]
    // if L = 0, sum of subarray [L,R] = prefixSums[R]
    // for a given R, we want to find an L such that prefixSums[R] - prefixSum[L - 1] >= target -> prefixSums[L - 1] <= prefixSums[R] - target
    set<ll> frontier = {0}; // 0 is sentinel value for case where L = 0
    ll ans = (target <= 0) ? 0 : 1e18; // account for case where target is negative, and we can technically choose an empty subarray
    for (int i = 0; i < prefixSums.size(); i++) {
        ll T = prefixSums[i] - target;
        auto it = frontier.upper_bound(T);
        // edge case: if upper bound result is start of iterator, that means all elements in set is bigger than T
        if (it != frontier.begin()) {
            ll best_l = *prev(it);          // go back one step to find largest prefixSums[L - 1] <= prefixSums[R] - target
            ans = min(ans, prefixSums[i] - best_l);
        }
        frontier.insert(prefixSums[i]);
    }
    return ans;
}
 
ll max_subarray_sum(const vector<ll>& arr) {
    ll current_max = arr[0], global_max = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        current_max = max(arr[i], current_max + arr[i]);
        global_max = max(global_max, current_max);
    }
    return global_max;
}

ll min_subarray_sum(const vector<ll>& arr) {
    ll current_min = arr[0], global_min = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        current_min = min(arr[i], current_min + arr[i]);
        global_min = min(global_min, current_min);
    }
    return global_min;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n, m;
    ll h, d;
    cin >> n >> m >> h >> d;
 
    vector<ll> c(n), enemies(m);
    for (auto& x : c) cin >> x;
    for (auto& x : enemies) cin >> x;
 
    ll dStar = damageNeeded(h, enemies);
    ll target = dStar - d;
    
    // use Kadane's to find maximum and minimum subarray sums in O(n) time
    // note that we are allowed to choose nothing
    ll best = max(0ll,max_subarray_sum(c)), worst = min(0ll,min_subarray_sum(c));
    if (best < target) {
        cout << "Of erfitt!\n";
    } else if (worst >= target) {
        cout << "Of audvelt!\n";
    } else {
        cout << cheapestAtLeast(c, target) << " er matulegt\n";
    }
    return 0;
}