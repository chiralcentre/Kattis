#include <bits/stdc++.h>

using namespace std;

double a,b,c;

int main() {
    scanf("%lf\n%lf\n%lf",&a,&b,&c);
    double s = (a + b + c) / 2.0;
    printf("%.15lf\n", sqrt(s * (s - a) * (s - b) * (s -c)));
    return 0;
}