#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
#include <cmath>


using namespace std;

double V,t,a,b,h; int N,ans;

double f(double a, double b, double x) {
    double value = a * exp(-x * x) + b * sqrt(x);
    return value * value;    
}

// use simpson's rule for each sub interval
double simpson(double a, double b, double h) {
    // use 1 million subintervals
    double ans = 0, d = h / 1000000;
    double p = 0; 
    for (int i = 0; i < 1000000; i++) {
        ans += (f(a,b,p) + 4 * f(a,b,p + d / 2) + f(a,b,p + d)) * d / 6;
        p += d;
    }
    return ans;
}

int main() {
    scanf("%lf %d",&V,&N);
    scanf("%lf %lf %lf",&a,&b,&h);
    t = simpson(a,b,h) * M_PI, ans = 0;
    // printf("Volume = %lf\n", t);
    for (int i = 0; i < N - 1; i++) {
        scanf("%lf %lf %lf",&a,&b,&h);
        double v = simpson(a,b,h) * M_PI;
        // printf("Volume = %lf\n", v);
        if (abs(V - v) < abs(V - t)) {
            t = v, ans = i + 1;
        }
    }
    printf("%d\n",ans);
    return 0;
}