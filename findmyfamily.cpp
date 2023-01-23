#include <bits/stdc++.h>
#include <set>

using namespace std;

typedef set<int> si;
typedef vector<int> vi;

int main() {
    int k; scanf("%d",&k);
    vi ans;
    for (int i = 1; i <= k; i++) {
        int n; scanf("%d",&n);
        //largest[i] stores largest value on the right of index i in lst
        vi lst(n,0), largest(n,0);
        for (int j = 0; j < n; j++) scanf("%d", &lst[j]);
        int highest = -1;
        for (int j = n - 1; j > 0; j--) {
            highest = max(highest,lst[j]);
            largest[j - 1] = highest;
        }
        //printf("DEBUG: largest arr = ");
        //for (int j = 0; j < n; j++) printf("%d ",largest[j]);
        //go from left to right and keep track of all values seen thus far
        //at every index, with value v, find smallest element in set that is larger than v
        //a 2 1 3 ordering exists if smallest larger element on the left is smaller than largest element on the right
        si seen;
        for (int j = 0; j < n; j++) {
            auto it = seen.upper_bound(lst[j]);
            if (it != seen.end() && (*it) < largest[j]) {
                ans.push_back(i);
                break;
            }
            seen.insert(lst[j]);
        }
    }
    sort(ans.begin(), ans.end());
    printf("%d\n",ans.size());
    for (int m: ans) printf("%d\n",m);
    return 0;
}