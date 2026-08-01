#define _USE_MATH_DEFINES // Must be before <cmath> for some compilers
#include <bits/stdc++.h>

using namespace std;

double d;

int main() {
    scanf("%lf",&d);
    printf("%.12lf\n",(2.0 / 3.0) * M_PI * pow(d / 2, 3));
    return 0;
}