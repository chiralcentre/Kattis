#include <bits/stdc++.h>

using namespace std;

int N,a,ans = -1;

int main() {
    scanf("%d",&N);
    for (int i = 0; i < N; i++) {
        scanf("%d",&a);
        ans = max(a, ans);
    }
    printf("%d\n",ans);
    return 0;
}