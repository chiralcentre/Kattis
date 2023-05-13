#include <bits/stdc++.h>

using namespace std;

double X,Y,N,r,b;

int main() {
    while (true) {
        scanf("%lf %lf %lf %lf",&X,&Y,&N,&r);
        if (X == 0 && Y == 0 && N == 0 && r == 0) break;
        b = (r != 0 ? X * pow(1 + (r / 1200), N * 12) - (1200 * Y * (pow(1 + (r / 1200), N * 12)  - 1)) / r: X - 12 * N * Y);
        printf(b <= 0 ? "YES\n": "NO\n");
    }
    return 0;
}