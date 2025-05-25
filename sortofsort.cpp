#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int N,a;

int main() {
    scanf("%d",&N);
    vi ans;
    for (int i = 0; i < N; i++) {
        scanf("%d",&a);
        if (ans.empty() || a >= ans.back()) ans.push_back(a);
    }
    for (int i = 0; i < ans.size(); i++) {
        printf("%d",ans[i]);
        if (i < ans.size() - 1) printf(" ");
    }
    return 0;
}