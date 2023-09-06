#include <bits/stdc++.h>

using namespace std;

int t,s;

int main() {
    scanf("%d %d",&t,&s);
    vector<int> duration(s,0);
    for (int i = 0; i < s; i++) scanf("%d",&duration[i]);
    sort(duration.begin(), duration.end());
    int end = t * 60, ans = 0;
    for (int p: duration) {
        if (ans + p <= end) ans += p;
        else break;
    }
    printf("%d\n",ans);
    return 0;
}