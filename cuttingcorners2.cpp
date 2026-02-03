#include <bits/stdc++.h>

using namespace std;

double w,h;

int main() {
    scanf("%lf %lf",&w,&h);
    double H = sqrt(w * w + h * h);
    printf("%lf\n", w + h - H);
    return 0;
}