#include <bits/stdc++.h>

using namespace std;

double d,w,r1,r2,r3,D;

int main() {
    scanf("%lf %lf %lf %lf %lf",&d,&w,&r1,&r2,&r3);
    D = (d / (w + r1)) * r1 * 2 + (d / (w + r2)) * r2 * 2 + (d / (w + r3)) * r3 * 2;
    printf("%d\n", int(round(D)));
    return 0;
}