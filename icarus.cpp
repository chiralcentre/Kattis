#include <bits/stdc++.h>

using namespace std;

double D,R,x,y,a,b,c;

int main() {
    scanf("%lf %lf %lf %lf\n%lf %lf %lf",&D,&R,&x,&y,&a,&b,&c);
    double d = abs(a * x + b * y + c) / sqrt(a * a + b * b);
    (d <= R + D) ? printf("his wings melted\n") : printf("icarus lives on\n");
    return 0;
}