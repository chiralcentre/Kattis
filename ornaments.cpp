#include <bits/stdc++.h>

using namespace std;

const double PI = 3.141592653589793238463;

int r,h,s;

// add arc length to two times tangent length
int main() {
    while (true) {
        scanf("%d %d %d",&r,&h,&s);
        if (r + h + s == 0) break; // all three numbers are zeroes
        double angle = 2 * (PI - acos(double(r)/double(h)));
        printf("%.2lf\n", (2 * sqrt(h * h - r * r) + angle * r) / 100.0 * (100.0 + s));
    }
    return 0;
}