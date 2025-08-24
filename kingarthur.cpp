#include <bits/stdc++.h>

using namespace std;

double d,w,n;

int main() {
    scanf("%lf %lf %lf",&d,&w,&n);
    double circumference = d * M_PI;
    (circumference >= w * n) ? printf("YES\n") :printf("NO\n");
    return 0;
}