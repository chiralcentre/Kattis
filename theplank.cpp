#include <bits/stdc++.h>

using namespace std;

int n;

int fib(int n) {
    vector<int> ans = {0,1,2,4};
    for (int i = 4; i <= n; i++) ans.push_back(ans[i - 1] + ans[i - 2] + ans[i - 3]);
    return ans[n];
}

int main() {
    scanf("%d",&n);
    printf("%d\n",fib(n));
    return 0;
}