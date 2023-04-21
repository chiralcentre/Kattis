#include <bits/stdc++.h>

using namespace std;

int a,b,c,d;

int main() {
    int ce = 1;
    while (scanf("%d %d\n %d %d", &a, &b, &c, &d) == 4) {
        int D = a * d - b * c;
        int a11 = d / D, a12 = -b / D, a21 = -c / D, a22 = a / D;
        printf("Case %d:\n%d %d\n%d %d\n",ce++,a11,a12,a21,a22);
    }
    return 0;
}