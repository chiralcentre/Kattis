#include <bits/stdc++.h>

using namespace std;

double v,a,t;

int main() {
    scanf("%lf %lf %lf",&v,&a,&t);
    printf("%lf\n", v * t + 0.5 * a * t * t);
    return 0;
}