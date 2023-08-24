#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <cmath>

using namespace std;

double D,d,s;

int main() {
    int n; scanf("%d",&n);
    while (n--) {
        scanf("%lf %lf %lf",&D,&d,&s);
        double R = D / 2.0, r = d / 2.0;
        double a = (R - r) * (R - r);
        // assume the two centres and the line segment representing s are collinear
        double theta = acos((2 * a - (s + 2 * r) * (s + 2 * r)) / (2 * a));
        int ans = floor(2 * M_PI / theta);
        printf("%d\n", ans);
    }
    return 0;
}