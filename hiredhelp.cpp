#include <bits/stdc++.h>
#include <set>

using namespace std;
typedef multiset<int> msi;

int main() {
    int N,K; scanf("%d %d",&N,&K);
    vector<int> t(N,0);
    for (int i = 0; i < N; i++) scanf("%d",&t[i]);
    // multiset is used since there can be multiple same deadlines
    msi deadlines(t.begin(),t.end());
    int ans = 0;
    while (!deadlines.empty()) {
        msi::iterator iter = deadlines.begin();
        int elem = *iter, taken = 1; // deference iterator
        deadlines.erase(iter); // remove deadlines
        while (!deadlines.empty() && taken < K) {
            if (elem == taken) elem++; // +1 to find next higher element
            iter = deadlines.lower_bound(elem); 
            if (iter == deadlines.end()) break; // higher element not found
            elem = *iter;
            deadlines.erase(iter);
            taken++;
        }
        if (taken == K) ans++;
    }
    printf("%d\n",ans);
    return 0;
}