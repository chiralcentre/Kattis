#include <bits/stdc++.h>

using namespace std;

int n; double d,r1,r2,area = 0;

int main() {
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%lf %lf %lf",&d,&r1,&r2);
        area += M_PI * (r2 * r2 - r1 * r1) * (d / 360.0);
    }
    printf("%lf\n",area);
    return 0;
}