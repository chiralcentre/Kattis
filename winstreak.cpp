#include <bits/stdc++.h>

using namespace std;

int N,S,T;

int main() {
    scanf("%d",&N);
    int ans = 0,curr = 0;
    for (int i = 0; i < N; i++) {
        scanf("%d %d",&S,&T);
        if (S > T) {
            curr++;
            ans = max(curr, ans);
        } else {
            curr = 0;
        }
    }
    printf("%d\n",ans);
    return 0;
}