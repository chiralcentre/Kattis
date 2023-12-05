#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef unordered_map<int,int> umii;

int n,a,b;

int main() {
    scanf("%d",&n);
    umii seen;
    for (int i = 0; i < (n >> 1) + 1; i++) {
        scanf("%d %d",&a,&b);
        seen[a]++; seen[b]++;
    }
    vector<int> extra;
    for (auto &[k,v]: seen) {
        if (v == 2) extra.push_back(k);
    }
    a = min(extra[0], extra[1]), b = max(extra[0], extra[1]);
    printf("%d %d\n",a,b);
    return 0;
}