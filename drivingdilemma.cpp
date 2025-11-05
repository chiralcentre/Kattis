#include <bits/stdc++.h>

using namespace std;

double S,D,T;

int main() {
    scanf("%lf\n%lf\n%lf\n",&S,&D,&T);
    // convert to feet per second
    S *= 5280.0 / 3600.0;
    double t = D / S;
    (t <= T) ? printf("MADE IT\n") : printf("FAILED TEST\n");
    return 0;
}