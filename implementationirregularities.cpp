#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

int main() {
    int n; scanf("%d",&n);
    vi t(n,0); vpii s;
    for (int i = 0; i < n; i++) scanf("%d",&t[i]);
    for (int i = 0; i < n; i++) {
        int c; scanf("%d",&c);
        if (c > -1) s.push_back(make_pair(c,i));
    }
    //default sort function sorts by first element
    sort(s.begin(), s.end());
    int ans = -1, total = 0;
    for (pii p: s) {
        total += t[p.second];
        int temp = total % p.first == 0 ? total / p.first : total / p.first + 1;
        ans = max(temp, ans);
    }
    printf("%d\n",ans);
    return 0;
}