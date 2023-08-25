#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <cmath>

using namespace std;

int T,n; double r;

int main() {
    scanf("%d",&T);
    while (T--) {
        scanf("%lf %d",&r,&n);
        double area = M_PI * r * r;
        double currarea = M_PI * r * r;
        for (int i = 0; i < n - 1; i++) {
            area += currarea;
            currarea *= 0.75;
        }
        printf("%lf\n",area);
    }
    return 0;
}