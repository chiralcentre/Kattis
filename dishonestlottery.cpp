#include <bits/stdc++.h>

using namespace std;

typedef unordered_map<int,int> umii;
typedef vector<int> vi;

int n,x; 

int main() {
    scanf("%d",&n);
    umii freq;
    for (int i = 0; i < 10 * n; i++) {
        for (int j = 0; j < 5; j++) {
            scanf("%d",&x);
            freq[x]++;
        }
    }
    vi ans;
    for ( const auto &[key, value]: freq ) {
        if (value > (n << 1)) ans.push_back(key);
    }
    sort(ans.begin(),ans.end());
    if (ans.size() == 0) printf("-1\n");
    else {
        for (int i = 0; i < ans.size(); i++) {
            printf("%d",ans[i]);
            if (i < ans.size() - 1) printf(" ");
        }
        printf("\n");
    }
    return 0;
}