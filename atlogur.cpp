#include <bits/stdc++.h>

using namespace std;

int n;

int h[1000],s[1000];

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) scanf("%d %d",&h[i],&s[i]);
    int winner = 0;
    for (int i = 1; i < n; i++) {
        int a = h[winner] / s[i] + (h[winner] % s[i] != 0);
        int b = h[i] / s[winner] + (h[i] % s[winner] != 0);
        // a represents number of hits to beat knight winner by knight i
        // b represents number of hits to beat knight i by knight winner
        // printf("a = %d, b = %d, i = %d, w = %d\n", a,b,i,winner);
        if (b > 1) {
            if (b <= a) { // knight winner wins
                h[winner] -= (b - 1) * s[i];
            } else { // knight i wins
                h[i] -= a * s[winner];
                winner = i;
            }
        }
    }
    printf("%d\n",winner + 1);
    return 0;
}