#include <bits/stdc++.h>

using namespace std;

double x,y; int r;

string solve(double x, double y, int r) {
    double a = 0, b = 0;
    for (int i = 0; i < r; i++) {
        double n = a * a - b * b;
        double u = 2 * a * b;
        n += x;
        u += y;
        a = n; b = u;
        if (a * a + b * b > 4.0) return "OUT";
    }
    return "IN";
}

int main() {
    int c = 1;
    while (scanf("%lf %lf %d",&x,&y,&r) == 3) {
        printf("Case %d: %s\n",c,solve(x,y,r).c_str());
        c++;
    }
    return 0;
}