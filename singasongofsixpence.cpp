#include <bits/stdc++.h>

using namespace std;

double R,r,h,b;

int main() {
    scanf("%lf\n%lf\n%lf\n%lf",&R,&r,&h,&b);
    double V = 3.14159 * h * (R * R + R * r + r * r) / 3.0;
    int ans = floor(V / b);
    printf("%d birds\n", ans);
    return 0;
}