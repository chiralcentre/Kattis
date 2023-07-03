#include <bits/stdc++.h>

using namespace std;

int N,R,ans = 1000000001;

//ans = minimum + 1
int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &R);
        ans = min(R, ans);
    }
    printf("%d\n", ans + 1);
    return 0;
}