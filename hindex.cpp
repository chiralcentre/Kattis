#include <bits/stdc++.h>

using namespace std;

int n,t; vector<int> citations(100000,0);

bool verify(int H) {
    int c = 0;
    for (int i = 0; i < n; i++) c += (citations[i] >= H);
    return c >= H;
}

// conduct binary search, total time complexity is O(n log n)
int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) scanf("%d",&citations[i]);
    int L = 0, H = n, ans = -1;
    while (L <= H) {
        int m = L + ((H - L) >> 1);
        if (verify(m)) {
            ans = m;
            L = m + 1;
        } else H = m - 1;
    }
    printf("%d\n",ans);
    return 0;
}