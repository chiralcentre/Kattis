#include <bits/stdc++.h>
#include <map>

using namespace std;

typedef map<int,int> mii;

int main() {
    mii freq;
    int N,Q; scanf("%d %d",&N,&Q);
    for (int i = 0; i < N; i++) {
        int a; scanf("%d",&a);
        //default value of 0
        //(freq[a] == 0) ? freq[a] = 1 : freq[a]++;
        freq[a]++;
    }
    mii::iterator it;
    for (int i = 0; i < Q; i++) {
        int T,D; scanf("%d %d",&T,&D);
        it = ((T == 1) ? freq.upper_bound(D) : freq.lower_bound(D));
        //make sure if element <= D for T == 2
        if (T == 2 && it != freq.begin() && (*it).first != D) --it;
        if (it == freq.end()) printf("-1\n");
        else {
            auto pair = *it;
            int u = pair.first;
            if (T == 2 && u > D) {
                printf("-1\n");
                continue;
            }
            if (--freq[u] == 0) freq.erase(pair.first);
            printf("%d\n",u);
        }
        //for (auto const&[k,v]: freq) printf("key = %d, value = %d\n",k,v);
    }
    return 0;
}