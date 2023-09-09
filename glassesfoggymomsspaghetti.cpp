#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <cmath>

using namespace std;

double d,x,y,h;

int main() {
    scanf("%lf %lf %lf %lf",&d,&x,&y,&h);
    double t1 = atan((y + h / 2) / x) - atan(y / x);
    double t2 = atan(y / x) - atan((y - h / 2) / x);
    printf("%lf\n",(tan(t1) + tan(t2)) * d);
    return 0;
}