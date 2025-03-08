#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

int n,d;

int main() {
    scanf("%d %d",&n,&d);
    vi pitch(n, 0);
    for (int i = 0; i < n; i++) scanf("%d",&pitch[i]);
    sort(pitch.begin(), pitch.end());
    int ans = 0, s = 0;
    while (s < n) {
        int j = s;
        while (j < n && pitch[j] - pitch[s] <= d) j++;
        s = j;
        ans++;
    }
    printf("%d\n", ans);
    return 0;
}