#include <bits/stdc++.h>

using namespace std;

int n,x;

int main() {
    scanf("%d",&n);
    unordered_set<int> seen;
    vector<int> res;
    for (int i = 0; i < n; i++) {
        scanf("%d",&x);
        if (seen.find(x) == seen.end()) {
            res.push_back(x);
            seen.insert(x);
        }
    }
    for (int i = 0; i < res.size(); i++) {
        printf("%d",res[i]);
        if (i < res.size() - 1) printf(" ");
    }
    printf("\n");
    return 0;
}