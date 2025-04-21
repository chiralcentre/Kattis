#include <bits/stdc++.h>

using namespace std;

int n,m;

// let number of sheep = x, number of humans = y
// x + y = n, 4x + 2y = m
// 2x = m - 2n
// x = (m - 2n) / 2
// y = n - (m - 2n) / 2 = 2n - m / 2
int main() {
    scanf("%d\n%d",&n,&m);
    if (m % 2 != 0) printf("Rong talning\n");
    else {
        int r = m - 2 * n;
        int y = 2 * n - m / 2;
        if (r % 2 != 0 || r < 0 || y < 0) printf("Rong talning\n");
        else printf("%d\n", r / 2);
    }
    return 0;
}