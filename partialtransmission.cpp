#include <bits/stdc++.h>

using namespace std;

int n,p,a;

int main() {
    scanf("%d\n%d",&n,&p);
    unordered_set<int> seq;
    for (int i = p; i < p + n; i++) seq.insert(i);
    for (int i = 0; i < n - 1; i++) {
        scanf("%d",&a);
        seq.erase(a);
    }
    printf("%d\n",*seq.begin());
    return 0;
}