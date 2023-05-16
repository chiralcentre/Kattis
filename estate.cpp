#include <bits/stdc++.h>

using namespace std;

int main() {
    int n = 1;
    while (true) {
        scanf("%d",&n);
        if (n == 0) break;
        int ans = 0;
        for (int i = 1; i * i <= 2 * n; i++) {
            if ((2 * n) % i == 0) {
                int t = (2 * n) / i - i + 1;
                if (t >= 4 && t % 2 == 0) ans ++;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}