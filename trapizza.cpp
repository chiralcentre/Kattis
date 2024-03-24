#include <bits/stdc++.h>

using namespace std;

double d,a,b,h,PI = 3.141592653589793238462643383279502884;

int main() {
    scanf("%lf\n%lf\n%lf\n%lf",&d,&a,&b,&h);
    if (d * d * PI > 2 * (a + b) * h) printf("Mahjong!\n");
    else if (d * d * PI < 2 * (a + b) * h) printf("Trapizza!\n");
    else printf("Jafn storar!\n");
    return 0;
}