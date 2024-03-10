#include <bits/stdc++.h>

using namespace std;

int n,c; int seen[7]= {0,0,0,0,0,0,0};

int modExp(int x, int y, int p) {
    int ans = 1;
    while (y > 0) {
        if (y % 2 == 1) ans *= x;
        ans %= p;
        y >>= 1;
        x *= x;
        x %= p;
    }
    return ans % p;
}

int main() {
    scanf("%d",&n);
    bool dupes = false;
    for (int i = 0; i < n; i++) {
        scanf("%d",&c);
        seen[c]++;
        if (seen[c] > 1) dupes = true;
    }
    int rem = modExp(6, 4 - n, 10000000);
    if (dupes) printf("0 %d\n", rem);
    else {
        int ash = 1, start = 6 - n;
        for (int i = 0; i < 4 - n; i++) ash *= start--;
        printf("%d %d\n", ash, rem - ash);
    }
    return 0;
}