#include <bits/stdc++.h>

using namespace std;

int n,lph;

int main() {
    scanf("%d %d",&n,&lph);
    vector<int> problems(n,0);
    for (int i = 0; i < n; i++) scanf("%d",&problems[i]);
    sort(problems.begin(), problems.end());
    int limit = 5 * lph, ans = 0;
    for (int i = 0; i < n; i++) {
        if (problems[i] <= limit) {
            limit -= problems[i];
            ans++;
        } else break;
    }
    printf("%d\n", ans);
    return 0;
}