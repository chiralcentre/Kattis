#include <bits/stdc++.h>

using namespace std;

int k,n,d;

int main() {
    scanf("%d %d",&n,&k);
    unordered_set<int> unique;
    for (int i = 0; i < n; i++) {
        scanf("%d",&d);
        unique.insert(d);
    }
    printf("%d\n",min(k,int(unique.size())));
    return 0;
}