#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef unordered_map<int,int> mii;

string solve(int q, int total, mii & prefixSums, vi & suffixSums) {
    if (q == 0 || q == total) return "Yes";
    if (q > total) return "No";
    for (int i = suffixSums.size() - 1; i >= 0; i--) {
        if (suffixSums[i] == q) return "Yes";
        if (suffixSums[i] < q) {
            int r = q - suffixSums[i];
            if (prefixSums.find(r) != prefixSums.end() && prefixSums[r] < i) {
                return "Yes";
            }
        } else return "No";
    }
    return "No";
}

int main() {
    int m,n; scanf("%d %d",&m,&n);
    vi stamps(m, 0), suffixSums(m + 1, 0);
    mii prefixSums;
    int total = 0;
    for (int i = 0; i < m; i++) {
        scanf("%d",&stamps[i]);
        total += stamps[i];
        prefixSums[total] = i;
    }
    int counter = 0;
    for (int i = m - 1; i >= 0; i--) {
        counter += stamps[i];
        suffixSums[i] = counter;
    }
    /*take note that suffixSum arrays is already in sorted order, with length m + 1.
    suffixSum is sorted in decreasing order
    for every query, check every suffix sum s <= q and check if q - s is a prefix sum that starts before the suffix sum
    prefixSums are stored in a hashtable, so check can be done in O(1)
    total time complexity is O(nm) */
    while (n--) {
        int q; scanf("%d",&q);
        printf("%s\n",solve(q,total,prefixSums,suffixSums).c_str());
    }
    return 0;
}