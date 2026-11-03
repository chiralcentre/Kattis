#include <bits/stdc++.h>

using namespace std;

int r,c;

int solve(int r, int c) {
    if (c == 1) return 1;
    if (r > 2) return -1;
    // at this point, r = 1 or r = 2
    if (r == 1) {
        return c / 3 + int(c % 3 > 0);
    } else if (r == 2) {
        return c / 2 + 1;
    } else {
        return -1;
    }
}

int main() {
    scanf("%d %d",&r,&c);
    printf("%d\n", solve(r,c));
    return 0;
}