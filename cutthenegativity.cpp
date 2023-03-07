#include <bits/stdc++.h>

using namespace std;

typedef tuple<int,int,int> iii;
typedef vector<iii> viii;

int main() {
    int n; scanf("%d",&n);
    viii ans;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int c; scanf("%d",&c);
            if (c > 0) ans.push_back(make_tuple(i,j,c));
        }
    }
    printf("%d\n", ans.size());
    for (iii t: ans) printf("%d %d %d\n",get<0>(t) + 1,get<1>(t) + 1,get<2>(t));
    return 0;
}